/* ============================================================
   ACTA (Team Resence) — FLAGSHIP APPLICATION CONTROLLER (v4.0)
   Single Page App Router, Micro-Donations (from ₹10),
   In-App Video Proof Engine, "My Donations" Hub, & Campus Guilds
   ============================================================ */

// ------------------------------------------------------------
// 1. DATA STORE & STATE
// ------------------------------------------------------------
const CAUSES_DATA = [
  {
    id: 1,
    title: "Nutritional Biscuit & Energy Pack",
    category: "meals",
    unitPrice: 10,
    unitName: "Biscuit Pack",
    goalUnits: 500,
    fundedUnits: 382,
    ngoName: "Jan Seva Foundation",
    ngoDarpan: "UP/2023/0182",
    location: "Surajpur Primary School, Greater Noida",
    desc: "Provides fortifying glucose and protein biscuits to undernourished children in Greater Noida slum schools.",
    thumb: "https://images.unsplash.com/photo-1599059813005-11265ba4b4ce?w=600&auto=format&fit=crop&q=80",
    icon: "🍪"
  },
  {
    id: 2,
    title: "Fresh Milk & Nutrition Sip",
    category: "meals",
    unitPrice: 25,
    unitName: "Milk Bottle (200ml)",
    goalUnits: 300,
    fundedUnits: 215,
    ngoName: "Bal Vikas Samiti",
    ngoDarpan: "UP/2022/0894",
    location: "Knowledge Park Slum Cluster, Greater Noida",
    desc: "Pure pasteurized milk packs distributed daily to infants and toddlers of migrant construction workers.",
    thumb: "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=600&auto=format&fit=crop&q=80",
    icon: "🥛"
  },
  {
    id: 3,
    title: "Warm Khichdi & Protein Meal",
    category: "meals",
    unitPrice: 50,
    unitName: "Full Hot Meal",
    goalUnits: 400,
    fundedUnits: 340,
    ngoName: "Roti Bank Greater Noida",
    ngoDarpan: "UP/2021/0441",
    location: "Pari Chowk Night Shelter, Greater Noida",
    desc: "Fresh, hygienic, warm dal-khichdi meals served in eco-friendly leaf bowls to daily wagers and pavement dwellers.",
    thumb: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop&q=80",
    icon: "🍲"
  },
  {
    id: 4,
    title: "Family Emergency Ration Kit (5kg)",
    category: "ration",
    unitPrice: 150,
    unitName: "5kg Ration Pack",
    goalUnits: 150,
    fundedUnits: 112,
    ngoName: "Gautam Buddha Nagar Relief Foundation",
    ngoDarpan: "UP/2023/0388",
    location: "Kasna Labor Colony, Greater Noida",
    desc: "Wholesale provision pack containing 2kg wholewheat atta, 1kg rice, 1kg dal, salt, and 500ml mustard oil.",
    thumb: "https://images.unsplash.com/photo-1584473457406-6240486418e9?w=600&auto=format&fit=crop&q=80",
    icon: "📦"
  },
  {
    id: 5,
    title: "Winter Warmth Blanket & Woolens",
    category: "winter",
    unitPrice: 250,
    unitName: "Heavy Wool Blanket",
    goalUnits: 200,
    fundedUnits: 168,
    ngoName: "Sheet Rahat Mission",
    ngoDarpan: "UP/2020/0912",
    location: "Alpha-1 Bus Stand & Depot, Greater Noida",
    desc: "Heavy thermal wool blankets distributed directly at night to elderly and destitute people sleeping on streets.",
    thumb: "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=600&auto=format&fit=crop&q=80",
    icon: "🧣"
  },
  {
    id: 6,
    title: "Primary First Aid & Child Hygiene Kit",
    category: "medical",
    unitPrice: 120,
    unitName: "Complete Hygiene Kit",
    goalUnits: 250,
    fundedUnits: 194,
    ngoName: "Swasthya Seva Trust",
    ngoDarpan: "UP/2024/0119",
    location: "Tugalpur Community Center, Greater Noida",
    desc: "Antiseptic Dettol, gauze dressings, soap bar, ORS sachets, and bandages for grassroots primary child care.",
    thumb: "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=600&auto=format&fit=crop&q=80",
    icon: "🩹"
  }
];

const CAMPUS_GUILDS = [
  {
    id: "glb-hostelb",
    name: "GL Bajaj Boys Hostel Block-B Guild",
    college: "GL Bajaj Institute of Technology & Management",
    members: 148,
    unitsFunded: 840,
    xp: 8400,
    rank: 1,
    streak: "🔥 14 Days",
    tagline: "Late night code, early morning community aid."
  },
  {
    id: "glb-bca3c",
    name: "GL Bajaj BCA Section 3C Guild",
    college: "GL Bajaj Institute of Management",
    members: 42,
    unitsFunded: 620,
    xp: 6200,
    rank: 2,
    streak: "🔥 8 Days",
    tagline: "Building ACTA from Section 3C to market."
  },
  {
    id: "glb-btechcs",
    name: "B.Tech CSE Innovators Clan",
    college: "GL Bajaj Institute of Technology & Management",
    members: 89,
    unitsFunded: 510,
    xp: 5100,
    rank: 3,
    streak: "🔥 6 Days",
    tagline: "Algorithmic social impact at Knowledge Park."
  },
  {
    id: "glb-alpha",
    name: "Girls Hostel Alpha Guild",
    college: "GL Bajaj Educational Campus",
    members: 76,
    unitsFunded: 490,
    xp: 4900,
    rank: 4,
    streak: "🔥 5 Days",
    tagline: "Empowering women and child nutrition."
  }
];

let userDonationsHistory = [
  {
    id: "ACTA-TX-9842",
    causeTitle: "Warm Khichdi & Protein Meal",
    units: 2,
    unitPrice: 50,
    total: 100,
    date: "12-Oct-2026",
    ngo: "Roti Bank Greater Noida",
    location: "Pari Chowk Shelter, Greater Noida",
    statusStage: 5, // 1 to 5
    statusText: "Verified & Archived with Video Proof",
    proofVideoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
    gps: "28.4744° N, 77.5040° E",
    invoiceId: "INV-2026-9042",
    hash: "a8f3b9c1482d7e0129e019b8821034"
  },
  {
    id: "ACTA-TX-9801",
    causeTitle: "Nutritional Biscuit & Energy Pack",
    units: 5,
    unitPrice: 10,
    total: 50,
    date: "10-Oct-2026",
    ngo: "Jan Seva Foundation",
    location: "Surajpur Primary School, Greater Noida",
    statusStage: 5,
    statusText: "Verified & Archived with Video Proof",
    proofVideoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
    gps: "28.4682° N, 77.4912° E",
    invoiceId: "INV-2026-8819",
    hash: "c24e891b0042a98f773b09214482b1"
  },
  {
    id: "ACTA-TX-9755",
    causeTitle: "Family Emergency Ration Kit (5kg)",
    units: 1,
    unitPrice: 150,
    total: 150,
    date: "08-Oct-2026",
    ngo: "Gautam Buddha Nagar Relief Foundation",
    location: "Kasna Labor Colony, Greater Noida",
    statusStage: 5,
    statusText: "Verified & Archived with Video Proof",
    proofVideoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
    gps: "28.4590° N, 77.5120° E",
    invoiceId: "INV-2026-8742",
    hash: "f991b2c45812a00192e478201b8742"
  }
];

let selectedCause = null;
let selectedUnits = 1;

// ------------------------------------------------------------
// 2. ROUTER MATRIX
// ------------------------------------------------------------
const routes = {
  '/': 'view-home',
  '/causes': 'view-causes',
  '/communities': 'view-communities',
  '/impact': 'view-impact',
  '/leaderboard': 'view-leaderboard',
  '/dashboard': 'view-dashboard',
  '/about': 'view-about',
  '/transparency': 'view-transparency',
  '/fcra': 'view-fcra'
};

function navigate(path, pushState = true) {
  let viewId = routes[path] || 'view-home';
  
  // Hide all views
  document.querySelectorAll('.view-container').forEach(el => {
    el.classList.add('hidden');
  });
  
  // Show target view
  const target = document.getElementById(viewId);
  if (target) {
    target.classList.remove('hidden');
  }

  // Update active nav link
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.getAttribute('href') === path) {
      a.classList.add('active');
    } else {
      a.classList.remove('active');
    }
  });

  if (pushState && window.location.pathname !== path) {
    history.pushState({ path }, '', path);
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.addEventListener('popstate', (e) => {
  const path = (e.state && e.state.path) || window.location.pathname || '/';
  navigate(path, false);
});

// Mobile menu toggle
function toggleMobileMenu() {
  const drawer = document.getElementById('mobileDrawer');
  if (drawer) {
    drawer.classList.toggle('active');
  }
}

// ------------------------------------------------------------
// 3. CAUSES RENDERING & FILTERING
// ------------------------------------------------------------
function renderCauseCard(c) {
  const pct = Math.min(100, Math.round((c.fundedUnits / c.goalUnits) * 100));
  return `
    <div class="cause-card">
      <div class="cause-card-thumb">
        <img src="${c.thumb}" alt="${c.title}" loading="lazy" />
        <div class="cause-unit-price-badge">₹${c.unitPrice} / unit</div>
      </div>
      <div class="cause-body">
        <div style="font-size:0.75rem; color:var(--emerald-light); font-weight:700; text-transform:uppercase; margin-bottom:6px;">
          ${c.icon} ${c.ngoName} • Darpan: ${c.ngoDarpan}
        </div>
        <div class="cause-title">${c.title}</div>
        <div class="cause-desc">${c.desc}</div>
        
        <div class="cause-progress-wrap">
          <div class="cause-progress-meta">
            <span style="color:var(--text-main);">${c.fundedUnits} of ${c.goalUnits} units funded</span>
            <span style="color:var(--emerald-light);">${pct}%</span>
          </div>
          <div class="progress-bar-bg">
            <div class="progress-bar-fill" style="width: ${pct}%;"></div>
          </div>
        </div>

        <button class="btn btn-primary btn-full" onclick="openDonateModal(${c.id})">
          <span>🍲</span>
          <span>Fund This Unit (₹${c.unitPrice})</span>
        </button>
      </div>
    </div>
  `;
}

function renderAllCauses(filter = 'all', containerId = 'homeCausesGrid') {
  const el = document.getElementById(containerId);
  if (!el) return;

  const filtered = filter === 'all' 
    ? CAUSES_DATA 
    : CAUSES_DATA.filter(c => c.category === filter);

  el.innerHTML = filtered.map(renderCauseCard).join('');
}

function filterCauses(cat, btn) {
  document.querySelectorAll('.filter-tab-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  renderAllCauses(cat, 'homeCausesGrid');
}

function filterCausesCatalog(cat, btn) {
  document.querySelectorAll('.filter-tabs .filter-tab-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  renderAllCauses(cat, 'catalogCausesGrid');
}

// ------------------------------------------------------------
// 4. ONE-CLICK INSTANT DONATION FLOW
// ------------------------------------------------------------
function openDonateModal(causeId) {
  const cause = CAUSES_DATA.find(c => c.id === causeId) || CAUSES_DATA[0];
  selectedCause = cause;
  selectedUnits = 1;

  document.getElementById('modalCauseTitle').innerText = cause.title;
  document.getElementById('modalCauseIcon').innerText = cause.icon;
  document.getElementById('modalCauseUnitPrice').innerText = `₹${cause.unitPrice} per ${cause.unitName}`;
  document.getElementById('donateUnits').value = 1;

  calcTotalDonation();
  document.getElementById('donateModal').classList.remove('hidden');
}

function closeDonateModal() {
  document.getElementById('donateModal').classList.add('hidden');
}

function adjustUnits(delta) {
  selectedUnits = Math.max(1, selectedUnits + delta);
  document.getElementById('donateUnits').value = selectedUnits;
  calcTotalDonation();
}

function setDonatePreset(amount) {
  if (!selectedCause) selectedCause = CAUSES_DATA[0];
  const units = Math.max(1, Math.round(amount / selectedCause.unitPrice));
  selectedUnits = units;
  document.getElementById('donateUnits').value = units;
  calcTotalDonation();
}

function calcTotalDonation() {
  const val = parseInt(document.getElementById('donateUnits').value, 10) || 1;
  selectedUnits = Math.max(1, val);
  const total = selectedUnits * (selectedCause ? selectedCause.unitPrice : 10);
  document.getElementById('modalTotalPayable').innerText = `₹${total.toFixed(2)}`;
}

function processMockUpi(appName) {
  showToast(`⚡ Launching ${appName} Instant 0% MDR UPI Intent...`, 'success');
}

function executeDonation() {
  if (!selectedCause) return;
  const total = selectedUnits * selectedCause.unitPrice;
  const txHash = 'acta_' + Math.random().toString(36).substring(2, 12);
  
  // Update cause units funded
  selectedCause.fundedUnits += selectedUnits;
  
  // Push to user donation history
  const newDonation = {
    id: 'ACTA-TX-' + Math.floor(1000 + Math.random() * 9000),
    causeTitle: selectedCause.title,
    units: selectedUnits,
    unitPrice: selectedCause.unitPrice,
    total: total,
    date: '15-Oct-2026',
    ngo: selectedCause.ngoName,
    location: selectedCause.location,
    statusStage: 5,
    statusText: 'Verified & Archived with Video Proof',
    proofVideoUrl: 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4',
    gps: '28.4744° N, 77.5040° E',
    invoiceId: 'INV-2026-' + Math.floor(1000 + Math.random() * 9000),
    hash: txHash
  };
  
  userDonationsHistory.unshift(newDonation);
  
  // Re-render
  renderAllCauses('all', 'homeCausesGrid');
  renderAllCauses('all', 'catalogCausesGrid');
  renderUserDonations();
  
  closeDonateModal();
  showToast(`🎉 ₹${total} Donated Successfully! 100% video proof & GST receipt generated.`, 'success');
  
  // Redirect to dashboard to view the donation
  setTimeout(() => {
    navigate('/dashboard');
  }, 1000);
}

// ------------------------------------------------------------
// 5. USER DASHBOARD ("MY DONATIONS")
// ------------------------------------------------------------
function renderUserDonations() {
  const el = document.getElementById('userDonationsList');
  if (!el) return;

  if (userDonationsHistory.length === 0) {
    el.innerHTML = `<div class="card-glass" style="text-align:center; padding:40px;">No donations recorded yet.</div>`;
    return;
  }

  el.innerHTML = userDonationsHistory.map((d, index) => {
    const aidSplit = (d.total * 0.95).toFixed(2);
    const feeSplit = (d.total * 0.05).toFixed(2);
    
    return `
      <div class="donation-row">
        <div class="donation-header-line">
          <div>
            <span class="badge badge-emerald" style="font-size:0.7rem; margin-bottom:4px;">${d.id}</span>
            <h4 style="font-size:1.15rem; margin:2px 0;">${d.causeTitle} (${d.units} units)</h4>
            <div style="font-size:0.8rem; color:var(--text-muted);">
              Partner NGO: <strong>${d.ngo}</strong> • Location: ${d.location}
            </div>
          </div>
          <div style="text-align:right;">
            <div style="font-family:var(--font-heading); font-size:1.4rem; font-weight:800; color:var(--emerald-light);">₹${d.total.toFixed(2)}</div>
            <div style="font-size:0.72rem; color:var(--text-dim);">₹${aidSplit} Ground Aid • ₹${feeSplit} Fee</div>
          </div>
        </div>

        <!-- 5-STAGE STATUS TRACKER -->
        <div class="status-tracker">
          <div class="status-step completed">
            <div class="status-step-dot">✓</div>
            <div class="status-step-title">Donation Logged</div>
          </div>
          <div class="status-step completed">
            <div class="status-step-dot">✓</div>
            <div class="status-step-title">NGO Assigned</div>
          </div>
          <div class="status-step completed">
            <div class="status-step-dot">✓</div>
            <div class="status-step-title">Procured Bulk</div>
          </div>
          <div class="status-step completed">
            <div class="status-step-dot">✓</div>
            <div class="status-step-title">In-App Video</div>
          </div>
          <div class="status-step completed">
            <div class="status-step-dot">✓</div>
            <div class="status-step-title">Verified</div>
          </div>
        </div>

        <!-- PROOF ACTIONS -->
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; border-top:1px solid var(--border); padding-top:12px;">
          <div style="font-size:0.78rem; color:var(--emerald-light); font-weight:600;">
            ✓ Live Camera Video Verified • NTP Timestamp: ${d.date}
          </div>
          <div style="display:flex; gap:8px;">
            <button class="btn btn-secondary btn-sm" onclick="openVideoProofModal('${d.id}')">
              <span>📹</span>
              <span>Watch Proof Video</span>
            </button>
            <button class="btn btn-secondary btn-sm" onclick="openInvoiceModalFromProof()">
              <span>🧾</span>
              <span>View GST Bill</span>
            </button>
            <button class="btn btn-ghost btn-sm" onclick="downloadAuditReceipt('${d.id}')">
              <span>📥</span>
              <span>Audit Receipt</span>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function switchDashTab(tabId, btn) {
  document.querySelectorAll('.filter-tabs .filter-tab-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');

  document.querySelectorAll('.dash-subtab').forEach(t => t.classList.add('hidden'));
  const target = document.getElementById('dashTab-' + tabId);
  if (target) target.classList.remove('hidden');
}

// ------------------------------------------------------------
// 6. VIDEO PROOF & INVOICE MODALS
// ------------------------------------------------------------
function openVideoProofModal(donationId) {
  const d = userDonationsHistory.find(x => x.id === donationId) || userDonationsHistory[0];
  document.getElementById('videoProofTitle').innerText = `${d.causeTitle} — Execution Proof`;
  document.getElementById('videoProofDate').innerText = `${d.date} • Greater Noida`;
  document.getElementById('hudGps').innerText = d.gps;
  document.getElementById('hudHash').innerText = d.hash.substring(0, 16) + '...';
  
  const modal = document.getElementById('videoProofModal');
  modal.classList.remove('hidden');
  
  const video = document.getElementById('proofVideoElem');
  if (video) {
    video.currentTime = 0;
    video.play().catch(() => {});
  }
}

function closeVideoProofModal() {
  const modal = document.getElementById('videoProofModal');
  modal.classList.add('hidden');
  const video = document.getElementById('proofVideoElem');
  if (video) video.pause();
}

function openInvoiceModalFromProof() {
  document.getElementById('invoiceModal').classList.remove('hidden');
}

function closeInvoiceModal() {
  document.getElementById('invoiceModal').classList.add('hidden');
}

function downloadAuditReceipt(donationId) {
  showToast('📄 Generating official cryptographic audit certificate PDF...', 'success');
  setTimeout(() => {
    window.print();
  }, 600);
}

// ------------------------------------------------------------
// 7. VOLUNTEER IN-APP CAMERA SIMULATOR
// ------------------------------------------------------------
let camMediaStream = null;
let camRecTimer = null;
let camSeconds = 0;

async function openVolunteerCameraModal() {
  const modal = document.getElementById('volunteerCameraModal');
  modal.classList.remove('hidden');
  
  const video = document.getElementById('volunteerCamVideo');
  try {
    // Attempt real camera stream
    camMediaStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    if (video) video.srcObject = camMediaStream;
  } catch (err) {
    console.warn("Using simulated video feed for camera viewfinder:", err.message);
    if (video) {
      video.src = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4";
      video.loop = true;
      video.play().catch(() => {});
    }
  }
}

function closeVolunteerCameraModal() {
  if (camMediaStream) {
    camMediaStream.getTracks().forEach(t => t.stop());
    camMediaStream = null;
  }
  if (camRecTimer) clearInterval(camRecTimer);
  document.getElementById('volunteerCameraModal').classList.add('hidden');
}

function startVolunteerRecording() {
  document.getElementById('btnStartRec').style.display = 'none';
  document.getElementById('btnStopRec').style.display = 'inline-flex';
  document.getElementById('camRecIndicator').style.display = 'inline-flex';
  
  camSeconds = 0;
  camRecTimer = setInterval(() => {
    camSeconds++;
    const mins = String(Math.floor(camSeconds / 60)).padStart(2, '0');
    const secs = String(camSeconds % 60).padStart(2, '0');
    document.getElementById('camRecTime').innerText = `REC ${mins}:${secs}`;
  }, 1000);
}

function stopVolunteerRecording() {
  clearInterval(camRecTimer);
  document.getElementById('btnStopRec').style.display = 'none';
  document.getElementById('camRecIndicator').style.display = 'none';
  document.getElementById('volunteerSubmitForm').style.display = 'block';
  showToast('📹 Video recorded & watermarked with live GPS telemetry!', 'success');
}

function submitVolunteerProof() {
  showToast('🚀 Proof uploaded & certified! Dispatched to donor dashboards.', 'success');
  setTimeout(() => {
    closeVolunteerCameraModal();
    navigate('/impact');
  }, 1000);
}

// ------------------------------------------------------------
// 8. ZERO-LEAKAGE UNIT ECONOMICS CALCULATOR
// ------------------------------------------------------------
function updateCalculator(val) {
  const amount = parseFloat(val) || 10;
  document.getElementById('calcInputAmount').value = amount;
  document.getElementById('calcSlider').value = Math.min(1000, amount);

  const aid = (amount * 0.95).toFixed(2);
  const fee = (amount * 0.05).toFixed(2);

  document.getElementById('calcAidValue').innerText = `₹${aid}`;
  document.getElementById('calcFeeValue').innerText = `₹${fee}`;
}

// ------------------------------------------------------------
// 9. CAMPUS GUILDS & LEADERBOARD RENDERING
// ------------------------------------------------------------
function renderGuilds() {
  const el = document.getElementById('guildsGrid');
  if (!el) return;

  el.innerHTML = CAMPUS_GUILDS.map(g => `
    <div class="card-glass">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <span class="badge badge-cyan">Rank #${g.rank}</span>
        <span style="font-size:0.8rem; font-weight:700; color:var(--amber);">${g.streak}</span>
      </div>
      <h3 style="font-size:1.2rem; margin-bottom:6px;">${g.name}</h3>
      <div style="font-size:0.8rem; color:var(--emerald-light); font-weight:600; margin-bottom:12px;">${g.college}</div>
      <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:16px;">${g.tagline}</p>
      
      <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:700; border-top:1px solid var(--border); padding-top:12px; margin-bottom:16px;">
        <span>${g.members} Members</span>
        <span style="color:var(--emerald-light);">${g.unitsFunded} Units Funded</span>
      </div>

      <button class="btn btn-secondary btn-full" onclick="showToast('🤝 Joined ${g.name}! Your contributions now boost your campus guild.', 'success')">
        Join Campus Guild
      </button>
    </div>
  `).join('');
}

function renderLeaderboard() {
  const tableBody = document.getElementById('leaderboardGuildsBody');
  if (tableBody) {
    tableBody.innerHTML = CAMPUS_GUILDS.map(g => `
      <tr ${g.rank === 1 ? 'class="highlight-acta"' : ''}>
        <td><strong style="color:var(--amber);">#${g.rank}</strong></td>
        <td><strong>${g.name}</strong><br><span style="font-size:0.75rem; color:var(--text-dim);">${g.college}</span></td>
        <td>${g.members}</td>
        <td style="font-weight:700; color:var(--emerald-light);">${g.unitsFunded} units</td>
        <td><code>${g.xp} XP</code></td>
      </tr>
    `).join('');
  }

  const streaksList = document.getElementById('leaderboardStreaksList');
  if (streaksList) {
    streaksList.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div><strong>Piyush Singh (Section 3C)</strong><br><span style="font-size:0.75rem; color:var(--text-dim);">GLBIM Greater Noida</span></div>
        <div style="color:var(--amber); font-weight:800;">🔥 19 Days</div>
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div><strong>Rohan Sharma (Hostel-B)</strong><br><span style="font-size:0.75rem; color:var(--text-dim);">GLBITM CSE</span></div>
        <div style="color:var(--amber); font-weight:800;">🔥 14 Days</div>
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div><strong>Sneha Verma (Hostel-Alpha)</strong><br><span style="font-size:0.75rem; color:var(--text-dim);">GLBITM IT</span></div>
        <div style="color:var(--amber); font-weight:800;">🔥 11 Days</div>
      </div>
    `;
  }
}

function renderProofFeed() {
  const el = document.getElementById('proofsGrid');
  if (!el) return;

  el.innerHTML = userDonationsHistory.map(d => `
    <div class="card-glass">
      <div style="position:relative; border-radius:8px; overflow:hidden; aspect-ratio:16/9; background:#000; margin-bottom:14px; cursor:pointer;" onclick="openVideoProofModal('${d.id}')">
        <video src="${d.proofVideoUrl}" muted loop style="width:100%; height:100%; object-fit:cover;"></video>
        <div style="position:absolute; inset:0; background:rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center;">
          <div style="width:48px; height:48px; border-radius:50%; background:var(--emerald); display:flex; align-items:center; justify-content:center; font-size:1.4rem; color:#061A14;">▶</div>
        </div>
        <div style="position:absolute; bottom:8px; left:8px; font-size:0.7rem; font-family:monospace; background:rgba(0,0,0,0.7); padding:2px 8px; border-radius:4px;">
          GPS: ${d.gps}
        </div>
      </div>

      <div style="font-size:0.75rem; color:var(--emerald-light); font-weight:700; text-transform:uppercase; margin-bottom:4px;">
        ${d.ngo} • Greater Noida
      </div>
      <h3 style="font-size:1.1rem; margin-bottom:6px;">${d.causeTitle}</h3>
      <p style="font-size:0.82rem; color:var(--text-muted); margin-bottom:14px;">
        Distribution completed on ${d.date} backed by wholesale invoice <code>#${d.invoiceId}</code>.
      </p>

      <div style="display:flex; gap:10px;">
        <button class="btn btn-secondary btn-sm" style="flex:1;" onclick="openVideoProofModal('${d.id}')">Watch Video</button>
        <button class="btn btn-ghost btn-sm" onclick="openInvoiceModalFromProof()">View Bill</button>
      </div>
    </div>
  `).join('');
}

function renderBadges() {
  const el = document.getElementById('userBadgesGrid');
  if (!el) return;

  const badges = [
    { icon: "🌟", title: "First Seed", desc: "Funded your very first ₹10 micro-donation." },
    { icon: "🍲", title: "Hunger Shield", desc: "Funded 10+ wholesome nutrition meals." },
    { icon: "🧣", title: "Winter Warmth", desc: "Shielded pavement dwellers with thermal woolens." },
    { icon: "🏛️", title: "Guild Pioneer", desc: "Active member of GL Bajaj BCA Section 3C." },
    { icon: "🔥", title: "Streak Master", desc: "Maintained a 5-day continuous giving habit." },
    { icon: "💯", title: "Century Impact", desc: "Achieved 100+ community impact points." }
  ];

  el.innerHTML = badges.map(b => `
    <div class="card-glass" style="text-align:center; padding:20px;">
      <div style="font-size:2.5rem; margin-bottom:8px;">${b.icon}</div>
      <h4 style="font-size:1.05rem; margin-bottom:4px;">${b.title}</h4>
      <p style="font-size:0.8rem; color:var(--text-muted);">${b.desc}</p>
      <span class="badge badge-emerald" style="margin-top:10px; font-size:0.65rem;">Unlocked</span>
    </div>
  `).join('');
}

function runAiAdvisor() {
  const budget = parseInt(document.getElementById('advisorBudget').value, 10) || 100;
  const biscuitUnits = Math.floor((budget * 0.4) / 10);
  const mealUnits = Math.floor((budget * 0.6) / 50);

  const res = document.getElementById('advisorResult');
  res.classList.remove('hidden');
  res.innerHTML = `
    <div style="background:rgba(16,185,129,0.1); border:1px solid var(--emerald-border); padding:16px; border-radius:8px;">
      <h4 style="color:var(--emerald-light); font-size:1rem; margin-bottom:6px;">Recommended ₹${budget}/Month Impact Allocation:</h4>
      <ul style="padding-left:18px; margin-bottom:10px; line-height:1.6;">
        <li>🍪 <strong>${biscuitUnits} Nutrition Biscuit Packs (₹10/ea)</strong> = ₹${biscuitUnits * 10} for school children</li>
        <li>🍲 <strong>${mealUnits} Full Warm Khichdi Meals (₹50/ea)</strong> = ₹${mealUnits * 50} for daily wagers</li>
      </ul>
      <div style="font-size:0.8rem; color:var(--text-dim);">
        95% (₹${(budget * 0.95).toFixed(2)}) goes directly to bulk food procurement backed by GST bills.
      </div>
    </div>
  `;
}

// ------------------------------------------------------------
// 10. TOAST NOTIFICATIONS
// ------------------------------------------------------------
function showToast(msg, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  t.innerHTML = `
    <span>${type === 'success' ? '✓' : '⚠️'}</span>
    <span>${msg}</span>
  `;

  container.appendChild(t);
  setTimeout(() => {
    t.style.opacity = '0';
    setTimeout(() => t.remove(), 300);
  }, 3500);
}

// ------------------------------------------------------------
// 11. INITIALIZATION
// ------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  renderAllCauses('all', 'homeCausesGrid');
  renderAllCauses('all', 'catalogCausesGrid');
  renderGuilds();
  renderLeaderboard();
  renderProofFeed();
  renderUserDonations();
  renderBadges();
  updateCalculator(100);

  // Initial path routing
  const initialPath = window.location.pathname || '/';
  navigate(initialPath, false);
});
