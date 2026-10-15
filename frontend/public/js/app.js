/* ============================================================
   ACTA (acta.resence.in) — OFFICIAL FLAGSHIP CONTROLLER (v6.0)
   Institutional Light Design System & Real-Time Escrow Verification
   Zero Unicode Emojis — 100% Crisp Monochromatic Lucide SVGs
   ============================================================ */

// --- LUCIDE SVG SPRITES ---
const ICONS = {
  check: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  shield_check: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>`,
  receipt: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/></svg>`,
  video: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/><rect x="2" y="6" width="14" height="12" rx="2"/></svg>`,
  file_text: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>`,
  download: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>`,
  award: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/></svg>`,
  flame: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>`,
  arrow_right: `<svg class="lucide-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>`
};

// ------------------------------------------------------------
// 1. DATA STORE (Itemized Micro-Causes Starting at ₹10)
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
    location: "Surajpur Primary School, Greater Noida",
    desc: "Provides fortifying glucose and protein biscuits to undernourished children in Greater Noida slum schools.",
    thumb: "https://images.unsplash.com/photo-1599059813005-11265ba4b4ce?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Child Nutrition"
  },
  {
    id: 2,
    title: "Fresh Toned Milk Pouch (500ml)",
    category: "meals",
    unitPrice: 25,
    unitName: "Milk Pouch (500ml)",
    goalUnits: 300,
    fundedUnits: 215,
    ngoName: "Bal Vikas Samiti",
    location: "Knowledge Park Slum Cluster, Greater Noida",
    desc: "Pure pasteurized milk packs distributed daily to infants and toddlers of migrant construction workers.",
    thumb: "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Infant Care"
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
    location: "Pari Chowk Night Shelter, Greater Noida",
    desc: "Fresh, hygienic, warm dal-khichdi meals served in eco-friendly leaf bowls to daily wagers and pavement dwellers.",
    thumb: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Direct Relief"
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
    location: "Kasna Labor Colony, Greater Noida",
    desc: "Wholesale provision pack containing 2kg wholewheat atta, 1kg rice, 1kg dal, salt, and 500ml mustard oil.",
    thumb: "https://images.unsplash.com/photo-1584473457406-6240486418e9?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Family Support"
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
    location: "Alpha-1 Bus Stand & Depot, Greater Noida",
    desc: "Heavy thermal wool blankets distributed directly at night to elderly and destitute people sleeping on streets.",
    thumb: "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Winter Shield"
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
    location: "Tugalpur Community Center, Greater Noida",
    desc: "Antiseptic Dettol, gauze dressings, soap bar, ORS sachets, and bandages for grassroots primary child care.",
    thumb: "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Health & Hygiene"
  }
];

// Campus Guilds Data
const GUILDS_DATA = [
  {
    id: "glb-hostel-b",
    name: "Boys Hostel Block-B",
    college: "GL Bajaj Institute of Technology & Management",
    members: 128,
    unitsFunded: 1420,
    rank: 1,
    tagline: "Championing daily midnight bread and biscuit drives across Pari Chowk.",
    xp: 7100
  },
  {
    id: "glb-bca-3c",
    name: "BCA Section 3C Guild",
    college: "GL Bajaj Institute of Management (GLBIM)",
    members: 42,
    unitsFunded: 620,
    rank: 2,
    tagline: "Founded by Piyush Singh & Team Resence — 100% verified grassroots giving.",
    xp: 3100
  },
  {
    id: "glb-btech-cse",
    name: "B.Tech CSE Code4Good",
    college: "GL Bajaj Institute of Technology & Management",
    members: 95,
    unitsFunded: 580,
    rank: 3,
    tagline: "Engineering students micro-allocating caffeine budgets to warm meals.",
    xp: 2900
  },
  {
    id: "glb-girls-alpha",
    name: "Girls Hostel Alpha",
    college: "GL Bajaj Campus Hostels",
    members: 64,
    unitsFunded: 440,
    rank: 4,
    tagline: "Dedicated to maternal nutrition and child education kit distribution.",
    xp: 2200
  }
];

// User Donation Audit History (State)
let userDonationsHistory = [
  {
    id: "ACTA-TX-9842",
    causeTitle: "Warm Khichdi & Protein Meal",
    units: 2,
    total: 100.00,
    ngo: "Roti Bank Greater Noida",
    location: "Pari Chowk Shelter, Greater Noida",
    date: "12-Oct-2026",
    gps: "28.4744° N, 77.5040° E",
    invoiceId: "GST-UP-2026-8812",
    hash: "0x89ab1024cd9e81254bf310ac90b",
    status: "Verified & Closed"
  },
  {
    id: "ACTA-TX-9801",
    causeTitle: "Nutritional Biscuit & Energy Pack",
    units: 5,
    total: 50.00,
    ngo: "Jan Seva Foundation",
    location: "Surajpur Primary School",
    date: "10-Oct-2026",
    gps: "28.5112° N, 77.4921° E",
    invoiceId: "GST-UP-2026-8419",
    hash: "0x77ba9104fa218cb4901ee19d28",
    status: "Verified & Closed"
  }
];

let activeCause = CAUSES_DATA[0];

// ------------------------------------------------------------
// 2. SPA ROUTER & CONSOLIDATED NAVIGATION
// ------------------------------------------------------------
function navigate(route, updateHistory = true) {
  const cleanRoute = (route || '/').split('?')[0].replace(/\/+$/, '') || '/';
  
  const routeMap = {
    '/': 'view-home',
    '/causes': 'view-causes',
    '/impact': 'view-impact',
    '/transparency': 'view-impact',
    '/communities': 'view-communities',
    '/leaderboard': 'view-communities',
    '/governance': 'view-governance',
    '/fcra': 'view-governance',
    '/about': 'view-governance'
  };

  const targetViewId = routeMap[cleanRoute] || 'view-home';

  document.querySelectorAll('.view-container').forEach(v => {
    v.classList.add('hidden');
  });

  const activeElem = document.getElementById(targetViewId);
  if (activeElem) {
    activeElem.classList.remove('hidden');
  }

  // Update navbar links
  document.querySelectorAll('.nav-links .nav-item').forEach(link => {
    const href = link.getAttribute('href');
    if (href === cleanRoute || (cleanRoute === '/transparency' && href === '/impact') || (cleanRoute === '/leaderboard' && href === '/communities')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  if (updateHistory && window.location.pathname !== cleanRoute) {
    window.history.pushState({ route: cleanRoute }, '', cleanRoute);
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.addEventListener('popstate', (e) => {
  const path = (e.state && e.state.route) ? e.state.route : window.location.pathname;
  navigate(path, false);
});

function toggleMobileMenu() {
  const drawer = document.getElementById('mobileDrawer');
  if (drawer) {
    drawer.classList.toggle('open');
  }
}

// ------------------------------------------------------------
// 3. SLIDE-OVER DRAWER (My Account & Donation Trail)
// ------------------------------------------------------------
function openSlideover() {
  renderSlideoverDonations();
  renderSlideoverBadges();
  document.getElementById('slideoverBackdrop').classList.add('open');
}

function closeSlideover(e) {
  document.getElementById('slideoverBackdrop').classList.remove('open');
}

function renderSlideoverDonations() {
  const el = document.getElementById('slideoverDonationsList');
  if (!el) return;

  el.innerHTML = userDonationsHistory.map(d => {
    const aid = (d.total * 0.95).toFixed(2);
    const fee = (d.total * 0.05).toFixed(2);

    return `
      <div style="background:var(--bg-subtle); border:1px solid var(--border); border-radius:var(--radius-sm); padding:14px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
          <div>
            <div style="font-weight:700; color:var(--text-main); font-size:0.92rem;">${d.causeTitle}</div>
            <div style="font-size:0.75rem; color:var(--text-muted);">${d.ngo} • ${d.date}</div>
          </div>
          <div style="text-align:right;">
            <div style="font-family:var(--font-heading); font-size:1.15rem; font-weight:800; color:var(--text-main);">₹${d.total.toFixed(2)}</div>
            <div style="font-size:0.68rem; color:var(--emerald); font-weight:600;">₹${aid} Aid • ₹${fee} Fee</div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border); padding-top:8px; margin-top:8px;">
          <span class="badge badge-emerald" style="font-size:0.65rem;">
            ${ICONS.shield_check}
            <span>100% Video Verified</span>
          </span>
          <div style="display:flex; gap:6px;">
            <button class="btn btn-secondary btn-sm" style="padding:4px 8px; font-size:0.75rem;" onclick="openVideoProofModal('${d.id}')">Video</button>
            <button class="btn btn-secondary btn-sm" style="padding:4px 8px; font-size:0.75rem;" onclick="openInvoiceModalFromProof()">Bill</button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function renderSlideoverBadges() {
  const el = document.getElementById('slideoverBadgesList');
  if (!el) return;

  const badges = [
    { title: "First Seed", desc: "Funded first ₹10 micro-unit" },
    { title: "Hunger Shield", desc: "10+ Wholesome meals" },
    { title: "Streak Master", desc: "5 continuous days" },
    { title: "Guild Pioneer", desc: "BCA 3C active leader" }
  ];

  el.innerHTML = badges.map(b => `
    <div style="background:var(--bg-subtle); border:1px solid var(--border); border-radius:var(--radius-sm); padding:10px; text-align:center;">
      <div style="color:var(--emerald); margin-bottom:4px;">${ICONS.award}</div>
      <div style="font-size:0.8rem; font-weight:700; color:var(--text-main);">${b.title}</div>
      <div style="font-size:0.7rem; color:var(--text-muted);">${b.desc}</div>
    </div>
  `).join('');
}

// ------------------------------------------------------------
// 4. CAUSES RENDERER
// ------------------------------------------------------------
function renderAllCauses(category = 'all', containerId = 'catalogCausesGrid') {
  const el = document.getElementById(containerId);
  if (!el) return;

  const filtered = category === 'all' 
    ? CAUSES_DATA 
    : CAUSES_DATA.filter(c => c.category === category);

  el.innerHTML = filtered.map(c => {
    const percent = Math.min(100, Math.round((c.fundedUnits / c.goalUnits) * 100));

    return `
      <div class="cause-card">
        <div class="cause-thumb">
          <img src="${c.thumb}" alt="${c.title}" loading="lazy" />
          <div class="cause-unit-pill">₹${c.unitPrice} / unit</div>
        </div>
        <div class="cause-body">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <span class="badge badge-slate">${c.badgeLabel}</span>
            <span style="font-size:0.76rem; color:var(--text-muted);">${c.location.split(',')[0]}</span>
          </div>
          <h3 class="cause-title">${c.title}</h3>
          <p class="cause-desc">${c.desc}</p>

          <div class="cause-progress-wrap">
            <div class="cause-progress-meta">
              <span>${c.fundedUnits} of ${c.goalUnits} units</span>
              <span style="color:var(--text-main); font-weight:700;">${percent}%</span>
            </div>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" style="width: ${percent}%;"></div>
            </div>
          </div>

          <div style="margin-top:auto;">
            <button class="btn btn-primary btn-full" onclick="openDonateModal(${c.id})">
              <span>Fund for ₹${c.unitPrice}</span>
              ${ICONS.arrow_right}
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function filterCauses(cat, btn) {
  document.querySelectorAll('.filter-tabs .filter-chip').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  renderAllCauses(cat, 'catalogCausesGrid');
}

// ------------------------------------------------------------
// 5. DONATE MODAL CONTROLLER
// ------------------------------------------------------------
function openDonateModal(causeId) {
  const cause = CAUSES_DATA.find(c => c.id === causeId) || CAUSES_DATA[0];
  activeCause = cause;

  document.getElementById('modalCauseTitle').innerText = `Sponsor: ${cause.title}`;
  document.getElementById('modalCauseDesc').innerText = `${cause.desc} Partner NGO: ${cause.ngoName}.`;

  setUnits(1);
  document.getElementById('donateModal').classList.remove('hidden');
}

function closeDonateModal() {
  document.getElementById('donateModal').classList.add('hidden');
}

function adjustUnits(delta) {
  const input = document.getElementById('donateUnitInput');
  let val = parseInt(input.value, 10) || 1;
  val = Math.max(1, Math.min(100, val + delta));
  input.value = val;
  updateModalTotal();
}

function setUnits(count) {
  const input = document.getElementById('donateUnitInput');
  input.value = count;
  updateModalTotal();
}

function updateModalTotal() {
  const input = document.getElementById('donateUnitInput');
  const units = parseInt(input.value, 10) || 1;
  const total = units * activeCause.unitPrice;
  const aid = (total * 0.95).toFixed(2);
  const fee = (total * 0.05).toFixed(2);

  document.getElementById('modalAidSplit').innerText = `₹${aid}`;
  document.getElementById('modalFeeSplit').innerText = `₹${fee}`;
  document.getElementById('modalTotalPayable').innerText = `₹${total.toFixed(2)}`;
}

function executeMockDonation() {
  const units = parseInt(document.getElementById('donateUnitInput').value, 10) || 1;
  const total = units * activeCause.unitPrice;
  const randomHex = Math.floor(Math.random() * 8999 + 1000);
  const newTxId = `ACTA-TX-${randomHex}`;

  userDonationsHistory.unshift({
    id: newTxId,
    causeTitle: activeCause.title,
    units: units,
    total: total,
    ngo: activeCause.ngoName,
    location: activeCause.location,
    date: "Today, Just Now",
    gps: "28.4744° N, 77.5040° E",
    invoiceId: `GST-UP-2026-${Math.floor(Math.random() * 8999 + 1000)}`,
    hash: `0x${Math.random().toString(16).substring(2, 10)}9f120`,
    status: "Verified & Closed"
  });

  renderAuditStream();
  closeDonateModal();
  showToast(`₹${total.toFixed(2)} Authorized! 100% video proof & GST invoice linked.`, 'success');
  openSlideover();
}

// ------------------------------------------------------------
// 6. LIVE AUDIT & PROOF STREAM CONTROLLER
// ------------------------------------------------------------
function renderAuditStream() {
  const el = document.getElementById('auditStreamContainer');
  if (!el) return;

  el.innerHTML = userDonationsHistory.map(d => {
    const aid = (d.total * 0.95).toFixed(2);
    const fee = (d.total * 0.05).toFixed(2);

    return `
      <div class="audit-stream-card">
        <div class="audit-stream-header">
          <div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
              <code>#${d.id}</code>
              <span class="badge badge-emerald">
                ${ICONS.shield_check}
                <span>${d.status}</span>
              </span>
            </div>
            <h3 style="font-size:1.22rem; font-weight:700; color:var(--text-main); margin-bottom:2px;">
              ${d.causeTitle} (${d.units} units)
            </h3>
            <div style="font-size:0.82rem; color:var(--text-muted);">
              Partner NGO: <strong>${d.ngo}</strong> • Ground Location: ${d.location}
            </div>
          </div>
          <div style="text-align:right;">
            <div style="font-family:var(--font-heading); font-size:1.6rem; font-weight:800; color:var(--text-main);">
              ₹${d.total.toFixed(2)}
            </div>
            <div style="font-size:0.75rem; color:var(--emerald); font-weight:600;">
              ₹${aid} Ground Aid • ₹${fee} Platform Fee
            </div>
          </div>
        </div>

        <!-- 5-Point Stepper Progression -->
        <div class="stepper-pipeline">
          <div class="stepper-step completed">
            <div class="stepper-dot">${ICONS.check}</div>
            <div class="stepper-title">Donation Logged</div>
          </div>
          <div class="stepper-step completed">
            <div class="stepper-dot">${ICONS.check}</div>
            <div class="stepper-title">NGO Assigned</div>
          </div>
          <div class="stepper-step completed">
            <div class="stepper-dot">${ICONS.check}</div>
            <div class="stepper-title">Bulk Procured</div>
          </div>
          <div class="stepper-step completed">
            <div class="stepper-dot">${ICONS.check}</div>
            <div class="stepper-title">In-App Video</div>
          </div>
          <div class="stepper-step completed">
            <div class="stepper-dot" style="background:var(--emerald); border-color:var(--emerald); color:#FFFFFF;">${ICONS.shield_check}</div>
            <div class="stepper-title" style="color:var(--emerald); font-weight:700;">NTP & GST Verified</div>
          </div>
        </div>

        <!-- Verification Actions -->
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; border-top:1px solid var(--border); padding-top:16px; margin-top:16px;">
          <div style="font-size:0.8rem; color:var(--emerald); font-weight:600; display:flex; align-items:center; gap:6px;">
            ${ICONS.shield_check}
            <span>Hardware Video Verified • GPS: ${d.gps}</span>
          </div>

          <div style="display:flex; gap:8px;">
            <button class="btn btn-secondary btn-sm" onclick="openVideoProofModal('${d.id}')">
              ${ICONS.video}
              <span>Watch Proof Video</span>
            </button>
            <button class="btn btn-secondary btn-sm" onclick="openInvoiceModalFromProof()">
              ${ICONS.file_text}
              <span>Inspect GST Bill</span>
            </button>
            <button class="btn btn-ghost btn-sm" onclick="downloadAuditReceipt('${d.id}')">
              ${ICONS.download}
              <span>Audit Certificate</span>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// ------------------------------------------------------------
// 7. VIDEO PROOF & INVOICE MODALS
// ------------------------------------------------------------
function openVideoProofModal(donationId) {
  const d = userDonationsHistory.find(x => x.id === donationId) || userDonationsHistory[0];
  document.getElementById('videoProofTitle').innerText = `${d.causeTitle} — Video Proof`;
  document.getElementById('videoProofDate').innerText = `${d.date} • ${d.location}`;
  document.getElementById('hudGps').innerText = d.gps;

  const modal = document.getElementById('videoProofModal');
  modal.classList.remove('hidden');

  const video = document.getElementById('proofVideoElem');
  if (video) {
    video.currentTime = 0;
    video.play().catch(() => {});
  }
}

function closeVideoProofModal() {
  document.getElementById('videoProofModal').classList.add('hidden');
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
  showToast('Generating official signed cryptographic audit certificate PDF...', 'success');
  setTimeout(() => {
    window.print();
  }, 400);
}

// ------------------------------------------------------------
// 8. VOLUNTEER IN-APP CAMERA CONTROLLER
// ------------------------------------------------------------
let camMediaStream = null;
let camRecTimer = null;
let camSeconds = 0;

async function openVolunteerCameraModal() {
  const modal = document.getElementById('volunteerCameraModal');
  modal.classList.remove('hidden');

  const video = document.getElementById('volunteerCamVideo');
  try {
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
  showToast('Video recorded & watermarked with live GPS telemetry!', 'success');
}

function submitVolunteerProof() {
  showToast('Proof certified & broadcast to donor dashboards.', 'success');
  setTimeout(() => {
    closeVolunteerCameraModal();
  }, 700);
}

// ------------------------------------------------------------
// 9. CAMPUS GUILDS CONTROLLER
// ------------------------------------------------------------
function renderGuilds() {
  const el = document.getElementById('guildsGrid');
  if (!el) return;

  el.innerHTML = GUILDS_DATA.map(g => `
    <div class="guild-card">
      <div style="display:flex; justify-content:space-between; align-items:flex-start;">
        <span class="badge badge-slate">Campus Rank #${g.rank}</span>
        <span style="font-family:var(--font-heading); font-size:1.1rem; font-weight:800; color:var(--emerald);">${g.xp} XP</span>
      </div>

      <div>
        <h3 style="font-size:1.2rem; font-weight:700; margin-bottom:2px; color:var(--text-main);">${g.name}</h3>
        <div style="font-size:0.8rem; color:var(--text-muted);">${g.college}</div>
      </div>

      <p style="font-size:0.84rem; color:var(--text-muted);">${g.tagline}</p>

      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border); padding-top:14px; margin-top:auto;">
        <div>
          <div style="font-family:var(--font-heading); font-size:1.15rem; font-weight:800; color:var(--text-main);">${g.unitsFunded} Units</div>
          <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">${g.members} Members Active</div>
        </div>
        <button class="btn btn-secondary btn-sm" onclick="showToast('Joined ${g.name}!', 'success')">
          <span>Join Guild</span>
        </button>
      </div>
    </div>
  `).join('');
}

// ------------------------------------------------------------
// 10. CANONICAL HOME LEDGER CALCULATOR
// ------------------------------------------------------------
function updateHomeLedger(val) {
  const amount = parseFloat(val) || 100;
  const aid = (amount * 0.95).toFixed(2);
  const fee = (amount * 0.05).toFixed(2);

  document.getElementById('homeCalcDisplay').innerText = `₹${Math.round(amount)}`;
  document.getElementById('homeCalcAid').innerText = `₹${aid}`;
  document.getElementById('homeCalcFee').innerText = `₹${fee}`;
}

// ------------------------------------------------------------
// 11. TOAST NOTIFICATIONS
// ------------------------------------------------------------
function showToast(msg, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  t.innerHTML = `
    <span style="color:var(--emerald);">${ICONS.shield_check}</span>
    <span>${msg}</span>
  `;

  container.appendChild(t);
  setTimeout(() => {
    t.style.opacity = '0';
    setTimeout(() => t.remove(), 300);
  }, 3500);
}

// ------------------------------------------------------------
// 12. INITIALIZATION
// ------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  renderAllCauses('all', 'homeCausesGrid');
  renderAllCauses('all', 'catalogCausesGrid');
  renderGuilds();
  renderAuditStream();
  updateHomeLedger(100);

  const initialPath = window.location.pathname || '/';
  navigate(initialPath, false);
});
