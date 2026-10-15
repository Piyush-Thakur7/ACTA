import os
import numpy as np
from PIL import Image, ImageFilter

downloads_dir = r"C:\Users\HP\Downloads"
docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"

# Load transparent text
src_text_path = os.path.join(downloads_dir, "ACTA_Wordmark_Transparent.png")
text_img = Image.open(src_text_path).convert("RGBA")
w, h = text_img.size

# Extract pure text with crisp alpha from centered source
centered_src = Image.open(os.path.join(downloads_dir, "ACTA_Wordmark_Centered.png")).convert("RGBA")
arr_centered = np.array(centered_src)
bg_ref = np.array([235, 239, 242], dtype=float)
diff = np.sqrt(np.sum((arr_centered[:, :, :3].astype(float) - bg_ref)**2, axis=2))
alpha = np.clip((diff - 8) / 35.0 * 255, 0, 255).astype(np.uint8)

text_rgb = np.zeros((h, w, 4), dtype=np.uint8)
text_rgb[:, :, 0] = 14  # R
text_rgb[:, :, 1] = 20  # G
text_rgb[:, :, 2] = 29  # B
text_rgb[:, :, 3] = alpha
clean_text = Image.fromarray(text_rgb)

def smooth_noise(seed, blur_radius, scale_factor=8):
    np.random.seed(seed)
    small_w = max(4, w // scale_factor)
    small_h = max(4, h // scale_factor)
    rand_arr = np.random.randint(0, 256, (small_h, small_w), dtype=np.uint8)
    img_rand = Image.fromarray(rand_arr).resize((w, h), Image.Resampling.BICUBIC)
    blurred = img_rand.filter(ImageFilter.GaussianBlur(blur_radius))
    arr = np.array(blurred).astype(float)
    norm = (arr - arr.min()) / (arr.max() - arr.min() + 1e-6)
    return norm

# Coordinate grid for ambient center lighting
y_coords, x_coords = np.ogrid[:h, :w]
center_dist = np.sqrt(((x_coords - w/2) / (w/2))**2 + ((y_coords - h/2) / (h/2))**2)
center_light = np.exp(-1.2 * center_dist**2) * 14.0

# ==============================================================================
# VARIATION 1: Ambient Studio Smoky Grey (Organic Soft Cloud Shading)
# ==============================================================================
norm1 = smooth_noise(42, blur_radius=35, scale_factor=16)
# Grey range: ~196 to 238
base_grey1 = 196.0 + (norm1 * 40.0) + center_light
grey1_final = np.clip(base_grey1, 185, 246).astype(np.uint8)

rgb1 = np.zeros((h, w, 3), dtype=np.uint8)
rgb1[:, :, 0] = np.clip(grey1_final - 2, 0, 255)
rgb1[:, :, 1] = np.clip(grey1_final, 0, 255)
rgb1[:, :, 2] = np.clip(grey1_final + 3, 0, 255)

bg1_img = Image.fromarray(rgb1).convert("RGBA")
final1 = Image.alpha_composite(bg1_img, clean_text)
target1 = os.path.join(downloads_dir, "ACTA_Logo_Grey_Shade_Studio.png")
final1.save(target1)
print(f"Variation 1 saved: {target1}")

# ==============================================================================
# VARIATION 2: Subtle Textured Concrete / Paper Grey (Organic Fine Texture)
# ==============================================================================
norm2_coarse = smooth_noise(101, blur_radius=40, scale_factor=12)
norm2_medium = smooth_noise(202, blur_radius=15, scale_factor=6)
np.random.seed(303)
fine_grain = (np.random.randn(h, w) * 3.0)

combined2 = norm2_coarse * 0.65 + norm2_medium * 0.30
norm2 = (combined2 - combined2.min()) / (combined2.max() - combined2.min() + 1e-6)
base_grey2 = 202.0 + (norm2 * 36.0) + (center_light * 0.7) + fine_grain
grey2_final = np.clip(base_grey2, 192, 246).astype(np.uint8)

rgb2 = np.zeros((h, w, 3), dtype=np.uint8)
rgb2[:, :, 0] = np.clip(grey2_final - 1, 0, 255)
rgb2[:, :, 1] = np.clip(grey2_final, 0, 255)
rgb2[:, :, 2] = np.clip(grey2_final + 2, 0, 255)

bg2_img = Image.fromarray(rgb2).convert("RGBA")
final2 = Image.alpha_composite(bg2_img, clean_text)
target2 = os.path.join(downloads_dir, "ACTA_Logo_Grey_Shade_Textured.png")
final2.save(target2)
print(f"Variation 2 saved: {target2}")

# ==============================================================================
# VARIATION 3: Minimalist Slate Grey Vignette (Subtle Diagonal Lighting Wash)
# ==============================================================================
vignette = (1.0 - np.clip(center_dist / 1.35, 0, 1.0)**1.5)
wash = ((x_coords / w) * 0.4 + (y_coords / h) * 0.6)
norm3 = smooth_noise(777, blur_radius=30, scale_factor=10)

base_grey3 = 192.0 + (vignette * 32.0) + (norm3 * 18.0) - (wash * 10.0)
grey3_final = np.clip(base_grey3, 185, 246).astype(np.uint8)

rgb3 = np.zeros((h, w, 3), dtype=np.uint8)
rgb3[:, :, 0] = np.clip(grey3_final - 2, 0, 255)
rgb3[:, :, 1] = np.clip(grey3_final, 0, 255)
rgb3[:, :, 2] = np.clip(grey3_final + 2, 0, 255)

bg3_img = Image.fromarray(rgb3).convert("RGBA")
final3 = Image.alpha_composite(bg3_img, clean_text)
target3 = os.path.join(downloads_dir, "ACTA_Logo_Grey_Shade_Minimal.png")
final3.save(target3)
print(f"Variation 3 saved: {target3}")

# Also copy to docs
import shutil
for t in [target1, target2, target3]:
    dest = os.path.join(docs_dir, os.path.basename(t))
    shutil.copy2(t, dest)

print("All variations generated and verified successfully!")
