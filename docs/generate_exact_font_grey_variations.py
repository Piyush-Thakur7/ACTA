import os
import numpy as np
from PIL import Image, ImageFilter

downloads_dir = r"C:\Users\HP\Downloads"
docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"

# Source original image uploaded by user
orig_path = r"C:\Users\HP\.gemini\antigravity\brain\0e435453-d970-4f11-8407-287e81b61280\.user_uploaded\media_1791713338079_edad394c.png"
orig_img = Image.open(orig_path).convert("RGB")
arr_orig = np.array(orig_img)
w, h = orig_img.size

# Extract exact text box (x: 435 to 825, y: 205 to 370)
text_h, text_w = 165, 390
text_box = arr_orig[205:205+text_h, 435:435+text_w].astype(float)
bg_orig = arr_orig[20, 20].astype(float)

# Normalized text mask (1.0 = background, 0.06 = dark text)
t_norm = np.clip(text_box / bg_orig, 0.0, 1.0)

# Coordinate grid for lighting
y_c, x_c = np.ogrid[:h, :w]
dist_c = np.sqrt(((x_c - w/2)/(w/2))**2 + ((y_c - h/2)/(h/2))**2)
spotlight = np.exp(-1.0 * dist_c**2) * 16.0

def make_smooth_noise(seed, blur_radius, scale_factor=10):
    np.random.seed(seed)
    sw = max(4, w // scale_factor)
    sh = max(4, h // scale_factor)
    rand_arr = np.random.randint(0, 256, (sh, sw), dtype=np.uint8)
    img_rand = Image.fromarray(rand_arr).resize((w, h), Image.Resampling.BICUBIC)
    blurred = img_rand.filter(ImageFilter.GaussianBlur(blur_radius))
    arr = np.array(blurred).astype(float)
    return (arr - arr.min()) / (arr.max() - arr.min() + 1e-6)

# ==============================================================================
# VARIATION 1: Ambient Studio Smoky Grey (Center Spotlight + Random Clouds)
# ==============================================================================
n1 = make_smooth_noise(42, blur_radius=32, scale_factor=14)
base_g1 = 196.0 + (n1 * 40.0) + spotlight
g1 = np.clip(base_g1, 185, 246)

c1 = np.zeros((h, w, 3), dtype=float)
c1[:, :, 0] = np.clip(g1 - 2, 0, 255)
c1[:, :, 1] = np.clip(g1, 0, 255)
c1[:, :, 2] = np.clip(g1 + 3, 0, 255)

# Center text
start_y = (h - text_h) // 2
start_x = (w - text_w) // 2
c1[start_y:start_y+text_h, start_x:start_x+text_w] *= t_norm

v1_img = Image.fromarray(c1.astype(np.uint8))
target1 = os.path.join(downloads_dir, "ACTA_Exact_Font_Grey_Studio.png")
v1_img.save(target1)
print(f"Saved: {target1}")

# ==============================================================================
# VARIATION 2: Textured Concrete / Paper Grey (Organic Fine Texture)
# ==============================================================================
n2_coarse = make_smooth_noise(101, blur_radius=36, scale_factor=10)
n2_med = make_smooth_noise(202, blur_radius=12, scale_factor=5)
np.random.seed(303)
fine_noise = np.random.randn(h, w) * 3.5

comb_n2 = n2_coarse * 0.65 + n2_med * 0.30
n2 = (comb_n2 - comb_n2.min()) / (comb_n2.max() - comb_n2.min() + 1e-6)
base_g2 = 202.0 + (n2 * 36.0) + (spotlight * 0.7) + fine_noise
g2 = np.clip(base_g2, 192, 246)

c2 = np.zeros((h, w, 3), dtype=float)
c2[:, :, 0] = np.clip(g2 - 1, 0, 255)
c2[:, :, 1] = np.clip(g2, 0, 255)
c2[:, :, 2] = np.clip(g2 + 2, 0, 255)

c2[start_y:start_y+text_h, start_x:start_x+text_w] *= t_norm

v2_img = Image.fromarray(c2.astype(np.uint8))
target2 = os.path.join(downloads_dir, "ACTA_Exact_Font_Grey_Textured.png")
v2_img.save(target2)
print(f"Saved: {target2}")

# ==============================================================================
# VARIATION 3: Minimalist Soft Grey Vignette
# ==============================================================================
vignette = (1.0 - np.clip(dist_c / 1.35, 0, 1.0)**1.5)
wash = ((x_c / w) * 0.4 + (y_c / h) * 0.6)
n3 = make_smooth_noise(777, blur_radius=28, scale_factor=10)

base_g3 = 192.0 + (vignette * 32.0) + (n3 * 18.0) - (wash * 10.0)
g3 = np.clip(base_g3, 185, 246)

c3 = np.zeros((h, w, 3), dtype=float)
c3[:, :, 0] = np.clip(g3 - 2, 0, 255)
c3[:, :, 1] = np.clip(g3, 0, 255)
c3[:, :, 2] = np.clip(g3 + 2, 0, 255)

c3[start_y:start_y+text_h, start_x:start_x+text_w] *= t_norm

v3_img = Image.fromarray(c3.astype(np.uint8))
target3 = os.path.join(downloads_dir, "ACTA_Exact_Font_Grey_Minimal.png")
v3_img.save(target3)
print(f"Saved: {target3}")

# Also copy to docs directory
import shutil
for t in [target1, target2, target3]:
    dest = os.path.join(docs_dir, os.path.basename(t))
    shutil.copy2(t, dest)

print("All exact-font grey background variations generated and saved!")
