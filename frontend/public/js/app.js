/* ============================================================
   ACTA by Resence — Master PRD v2.5 Controller (v10.0)
   Single-Source-of-Truth implementation of ACTA PRD Specifications
   ============================================================ */

// --- 1. THE 7 STANDARDIZED CAUSES (PRD Section 6.1) ---
const CAUSES_7 = [
  {
    id: 1,
    title: "Zero Hunger (Homeless & Stray Feeding)",
    scope: "Permanent Slot 1 • Infinite Cyclic Pool",
    unitCost: 35,
    unitName: "Hot Nutritious Meal",
    goalUnits: 1000,
    fundedUnits: 780,
    ngoName: "Jan Seva Foundation",
    location: "Surajpur Slum Clusters, Greater Noida",
    desc: "Fresh, hygienic dal-chawal and vegetable meals prepared daily and served in biodegradable bowls to daily wage migrant laborers.",
    thumb: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Child & Elder Nutrition",
    slaHours: "48h 12m"
  },
  {
    id: 2,
    title: "Green Earth (Campus & Highway Tree Plantation)",
    scope: "Permanent Slot 2 • Infinite Cyclic Pool",
    unitCost: 150,
    unitName: "Sapling & Guard",
    goalUnits: 300,
    fundedUnits: 210,
    ngoName: "NCR Vriksha Sanrakshan",
    location: "Knowledge Park III & Pari Chowk Corridor",
    desc: "Indigenous oxygen-rich Neem, Peepal, and Jamun saplings with iron protective tree guards maintained by student volunteers.",
    thumb: "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Urban Reforestation",
    slaHours: "72h 00m"
  },
  {
    id: 3,
    title: "Child Education (School Kits & Stationery)",
    scope: "Permanent Slot 3 • Infinite Cyclic Pool",
    unitCost: 250,
    unitName: "School Kit & Notebooks",
    goalUnits: 400,
    fundedUnits: 310,
    ngoName: "Bal Vikas Shiksha Samiti",
    location: "Kasna Primary Learning Center, Greater Noida",
    desc: "Complete kit containing 5 ruled notebooks, geometry set, pen-pencil pouch, and waterproof school backpack for primary students.",
    thumb: "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Youth Literacy",
    slaHours: "84h 30m"
  },
  {
    id: 4,
    title: "Elder Care (Essential Medicines & Hygiene)",
    scope: "Permanent Slot 4 • Infinite Cyclic Pool",
    unitCost: 300,
    unitName: "Monthly Medicine & Hygiene Pack",
    goalUnits: 150,
    fundedUnits: 118,
    ngoName: "Sheetal Aashray Vridhashram",
    location: "Alpha-1 Senior Care Home, Greater Noida",
    desc: "Essential geriatric maintenance medicines (blood pressure, diabetes strips, calcium), adult diapers, and antiseptic soaps.",
    thumb: "https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Senior Dignity",
    slaHours: "61h 45m"
  },
  {
    id: 5,
    title: "Women Empowerment (Monthly Dry Ration Hamper)",
    scope: "Permanent Slot 5 • Infinite Cyclic Pool",
    unitCost: 500,
    unitName: "Dry Ration Hamper (15kg)",
    goalUnits: 200,
    fundedUnits: 145,
    ngoName: "Stree Shakti Relief Trust",
    location: "Dankaur Village Women Cluster",
    desc: "Wholesale staple provision pack containing 5kg wholewheat flour, 5kg rice, 2kg dal, 1L mustard oil, salt, and spices for widow families.",
    thumb: "https://images.unsplash.com/photo-1584473457406-6240486418e9?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Household Food Security",
    slaHours: "90h 10m"
  },
  {
    id: 6,
    title: "Winter Warmth & Disaster Relief",
    scope: "Temporary Slot 1 • Seasonal Activation",
    unitCost: 250,
    unitName: "Thermal Fleece Blanket",
    goalUnits: 500,
    fundedUnits: 420,
    ngoName: "Sheet Rahat Abhiyan",
    location: "Depot & Auto Stand Pavements, Greater Noida",
    desc: "Heavy 2-ply thermal fleece blankets distributed at night to homeless elderly and rickshaw pullers sleeping on open pavements.",
    thumb: "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Cold Wave Shield",
    slaHours: "24h 00m"
  },
  {
    id: 7,
    title: "Emergency Stray Rescue & Veterinary Surgery",
    scope: "Temporary Slot 2 • Urgent Trauma Intervention",
    unitCost: 1500,
    unitName: "Veterinary Trauma Surgery",
    goalUnits: 20,
    fundedUnits: 16,
    ngoName: "Paws & Paws Greater Noida Shelter",
    location: "Pari Chowk Stray Animal Hospital",
    desc: "Emergency surgical treatment, fracture pinning, antibiotics, and post-operative foster boarding for street animals hit by vehicles.",
    thumb: "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=600&auto=format&fit=crop&q=80",
    badgeLabel: "Critical Life Support",
    slaHours: "18h 40m"
  }
];

// --- 2. THE 10-LEVEL EXPONENTIAL GIVING LADDER (PRD Section 10.2) ---
const XP_LADDER = [
  { level: "L01", title: "Seed Giver 🌱", xp: "0 – 4,999 XP", equiv: "₹0 – ₹499", perk: "Bronze Seed Tag. Unlocks on first ₹10 donation.", minXp: 0 },
  { level: "L02", title: "Kind Giver 🤝", xp: "5,000 – 11,999 XP", equiv: "₹500+", perk: "Silver Border Ring. Guild chat unlocked.", minXp: 5000 },
  { level: "L03", title: "Active Giver ⭐", xp: "12,000 – 24,999 XP", equiv: "₹1,200+", perk: "Polished Silver Ring + Guild shoutout badge.", minXp: 12000 },
  { level: "L04", title: "Impact Giver 🔷", xp: "25,000 – 49,999 XP", equiv: "₹2,500+", perk: "Sapphire Blue Ring + Voting power on next cause.", minXp: 25000 },
  { level: "L05", title: "Dedicated Giver 🛡️", xp: "50,000 – 99,999 XP", equiv: "₹5,000+", perk: "Gold Shield Ring + Featured on Campus Board.", minXp: 50000 },
  { level: "L06", title: "Community Pillar 🏛️", xp: "1,00,000 – 1,99,999 XP", equiv: "₹10,000+", perk: "Radiant Gold Ring + Authority to create Campus Guilds.", minXp: 100000 },
  { level: "L07", title: "Change Maker ⚔️", xp: "2,00,000 – 3,99,999 XP", equiv: "₹20,000+", perk: "Emerald Ring + Invite to annual NGO field audits.", minXp: 200000 },
  { level: "L08", title: "Master Benefactor 💎", xp: "4,00,000 – 6,99,999 XP", equiv: "₹40,000+", perk: "Ruby Ring + Priority sponsor matching on donations.", minXp: 400000 },
  { level: "L09", title: "Grand Philanthropist 🌟", xp: "7,00,000 – 9,99,999 XP", equiv: "₹70,000+", perk: "Glowing Amethyst Ring + City Hall of Fame Top Tier.", minXp: 700000 },
  { level: "L10", title: "The Crown Legend 👑", xp: "10,00,000+ XP", equiv: "₹1,00,000+", perk: "Animated Diamond Crown Ring + Resence Impact Award.", minXp: 1000000 }
];

// --- 3. CAMPUS GUILDS LEADERBOARD (PRD Section 10.3) ---
const GUILDS_DATA = [
  { rank: 1, name: "GL Bajaj Boys Hostel Block-B", college: "GL Bajaj Institute of Management", units: 840, members: 142, points: 8400, category: "hostels" },
  { rank: 2, name: "BCA Section 3C Changemakers", college: "GL Bajaj Institute of Management", units: 620, members: 98, points: 6200, category: "glbajaj" },
  { rank: 3, name: "B.Tech CSE Code4Good Clan", college: "GL Bajaj Group of Institutions", units: 580, members: 110, points: 5800, category: "glbajaj" },
  { rank: 4, name: "Sharda University Civic Club", college: "Sharda University, Greater Noida", units: 450, members: 76, points: 4500, category: "top" },
  { rank: 5, name: "Galgotias Rotaract Youth", college: "Galgotias University, Greater Noida", units: 390, members: 64, points: 3900, category: "top" }
];

// --- 4. ITEMISED USER DONATION AUDIT TRAIL ---
let userDonationsHistory = [
  {
    id: "ACTA-TX-98104",
    causeTitle: "Zero Hunger (Homeless & Stray Feeding)",
    units: 2,
    total: 70.00,
    ngo: "Jan Seva Foundation",
    location: "Surajpur Slum Clusters, Greater Noida",
    date: "Nov 5, 2026",
    gps: "28.4744° N, 77.5040° E",
    invoiceId: "GST-UP-2026-8910",
    status: "Verified & Closed",
    steps: ["Escrow Locked (UPI)", "Allocated to NGO", "Wholesale Procured", "Live Video Verified", "NTP & GST Audited"]
  },
  {
    id: "ACTA-TX-94218",
    causeTitle: "Child Education (School Kits & Stationery)",
    units: 1,
    total: 250.00,
    ngo: "Bal Vikas Shiksha Samiti",
    location: "Kasna Primary Learning Center",
    date: "Nov 3, 2026",
    gps: "28.4611° N, 77.5122° E",
    invoiceId: "GST-UP-2026-7412",
    status: "Verified & Closed",
    steps: ["Escrow Locked (UPI)", "Allocated to NGO", "Wholesale Procured", "Live Video Verified", "NTP & GST Audited"]
  },
  {
    id: "ACTA-TX-91042",
    causeTitle: "Green Earth (Campus & Highway Tree Plantation)",
    units: 1,
    total: 150.00,
    ngo: "NCR Vriksha Sanrakshan",
    location: "Knowledge Park III Corridor",
    date: "Oct 28, 2026",
    gps: "28.4689° N, 77.4988° E",
    invoiceId: "GST-UP-2026-6190",
    status: "Verified & Closed",
    steps: ["Escrow Locked (UPI)", "Allocated to NGO", "Wholesale Procured", "Live Video Verified", "NTP & GST Audited"]
  }
];

let activeCause = CAUSES_7[0];

// ============================================================
// 5. MASTER PILLAR NAVIGATION SWITCHER
// ============================================================
function switchPillar(pillarName) {
  const pillars = ['causes', 'proofs', 'xp', 'guilds', 'ledger'];
  pillars.forEach(p => {
    const sec = document.getElementById(`pillar_${p}`);
    const btn = document.getElementById(`tabBtn_${p}`);
    if (sec) {
      if (p === pillarName) {
        sec.classList.remove('hidden');
      } else {
        sec.classList.add('hidden');
      }
    }
    if (btn) {
      if (p === pillarName) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }
  });

  window.scrollTo({ top: 380, behavior: 'smooth' });
}

// ============================================================
// 6. RENDER THE 7 STANDARD CAUSES (PRD 6.1)
// ============================================================
function render7Causes() {
  const container = document.getElementById('causesGrid7');
  if (!container) return;

  container.innerHTML = CAUSES_7.map(c => {
    const percent = Math.min(100, Math.round((c.fundedUnits / c.goalUnits) * 100));

    return `
      <div class="cause-card-prd">
        <div class="cause-card-img-wrap">
          <img src="${c.thumb}" alt="${c.title}" loading="lazy" />
          <div class="cause-cost-pill">₹${c.unitCost} / Unit</div>
        </div>
        <div class="cause-card-content">
          <div class="cause-badge-row">
            <span class="badge badge-blue">${c.badgeLabel}</span>
            <span style="font-size:0.72rem; color:var(--text-muted);">${c.location.split(',')[0]}</span>
          </div>

          <h3 class="cause-card-title">${c.title}</h3>
          <p class="cause-card-desc">${c.desc}</p>

          <div class="cause-sla-box">
            <span>Execution SLA: <strong class="cause-sla-time">${c.slaHours}</strong></span>
            <span>${c.fundedUnits}/${c.goalUnits} Units (${percent}%)</span>
          </div>

          <div style="width:100%; height:5px; background:var(--bg-subtle); border-radius:3px; margin-bottom:12px; overflow:hidden;">
            <div style="width:${percent}%; height:100%; background:linear-gradient(90deg, #F97316, #10B981); border-radius:3px;"></div>
          </div>

          <!-- Quick Micro-Increment Chips -->
          <div class="cause-quick-chips">
            <button class="chip-inc" onclick="quickDonate(${c.id}, 1)">+₹${c.unitCost}</button>
            <button class="chip-inc" onclick="quickDonate(${c.id}, 2)">+2 Units</button>
            <button class="chip-inc featured" onclick="quickDonate(${c.id}, 5)">+5 Units (₹${c.unitCost * 5})</button>
          </div>

          <button class="btn btn-primary btn-full btn-sm" onclick="openDonateModal(${c.id})">
            <span>Sponsor Unit (₹${c.unitCost})</span>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

// ============================================================
// 7. RENDER PROOF STREAM & AUDIT TRAIL
// ============================================================
function renderProofs() {
  const container = document.getElementById('proofStreamList');
  if (!container) return;

  container.innerHTML = userDonationsHistory.map(d => {
    const aidSplit = (d.total * 0.90).toFixed(2);
    const feeSplit = (d.total * 0.10).toFixed(2);

    return `
      <div class="ledger-card">
        <div class="ledger-header">
          <div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
              <span class="telemetry-pulse"></span>
              <code>#${d.id}</code>
              <span class="badge badge-emerald">${d.status}</span>
            </div>
            <h3 style="font-size:1.15rem; margin-bottom:2px;">${d.causeTitle}</h3>
            <div style="font-size:0.8rem; color:var(--text-muted);">
              Partner NGO: <strong>${d.ngo}</strong> • Ground GPS: ${d.gps}
            </div>
          </div>

          <div style="text-align:right;">
            <div style="font-family:var(--font-heading); font-size:1.4rem; font-weight:800; color:var(--text-primary);">₹${d.total.toFixed(2)}</div>
            <div style="font-size:0.72rem; color:var(--emerald); font-weight:700;">₹${aidSplit} Direct Aid (90%)</div>
          </div>
        </div>

        <div class="stepper-pipeline-5">
          <div class="stepper-box done">1. Escrow (UPI)</div>
          <div class="stepper-box done">2. NGO Assigned</div>
          <div class="stepper-box done">3. Procured</div>
          <div class="stepper-box done">4. Video Stamped</div>
          <div class="stepper-box done">5. GST Audited</div>
        </div>

        <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:12px;">
          <button class="btn btn-secondary btn-sm" onclick="openVideoProofModal('${d.id}')">
            <span>📹 Watch Video Proof</span>
          </button>
          <button class="btn btn-secondary btn-sm" onclick="openInvoiceModal('${d.invoiceId}')">
            <span>🧾 Inspect GST Bill</span>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

// ============================================================
// 8. RENDER XP GIVING LADDER (PRD 10.2)
// ============================================================
function renderXpLadder() {
  const tbody = document.getElementById('xpLadderBody');
  if (!tbody) return;

  tbody.innerHTML = XP_LADDER.map(row => {
    const isCurrent = row.level === "L04";
    return `
      <tr class="${isCurrent ? 'active-tier' : ''}">
        <td><strong style="color:var(--primary); font-family:var(--font-heading);">${row.level}</strong></td>
        <td>
          <div style="font-weight:700; color:var(--text-primary);">${row.title}</div>
          <div style="font-size:0.75rem; color:var(--text-muted);">${row.perk}</div>
        </td>
        <td><code>${row.xp}</code></td>
        <td>${row.equiv}</td>
        <td>${isCurrent ? '<span class="badge badge-emerald">Current Level</span>' : '<span style="color:var(--text-dim); font-size:0.75rem;">Locked</span>'}</td>
      </tr>
    `;
  }).join('');
}

// ============================================================
// 9. RENDER CAMPUS GUILDS LEADERBOARD (PRD 10.3)
// ============================================================
let currentGuildFilter = 'all';

function filterGuilds(category, event) {
  currentGuildFilter = category;
  const pills = document.querySelectorAll('.guild-filter-pill');
  pills.forEach(p => p.classList.remove('active'));
  if (event && event.target) {
    event.target.classList.add('active');
  }
  renderGuilds();
}

function renderGuilds() {
  const container = document.getElementById('guildsLeaderboardList');
  if (!container) return;

  const filtered = GUILDS_DATA.filter(g => {
    if (currentGuildFilter === 'all') return true;
    if (currentGuildFilter === 'glbajaj') return g.college.includes("GL Bajaj");
    if (currentGuildFilter === 'hostels') return g.name.toLowerCase().includes("hostel") || g.category === "hostels";
    if (currentGuildFilter === 'top') return g.rank <= 5;
    return true;
  });

  container.innerHTML = filtered.map(g => `
    <div class="guild-card">
      <div style="display:flex; align-items:center; gap:16px;">
        <div class="guild-rank">#${g.rank}</div>
        <div>
          <div style="font-weight:800; font-size:1.05rem; color:var(--text-primary);">${g.name}</div>
          <div style="font-size:0.78rem; color:var(--text-muted);">${g.college}</div>
        </div>
      </div>
      <div style="display:flex; align-items:center; gap:18px;">
        <div style="text-align:right;">
          <div style="font-family:var(--font-heading); font-weight:800; color:var(--text-primary);">${g.units} Units</div>
          <div style="font-size:0.72rem; color:var(--text-muted);">${g.members} Active Students</div>
        </div>
        <button class="btn btn-secondary btn-sm" onclick="showToast('Joined ${g.name} Clan!', 'success')">Join Clan</button>
      </div>
    </div>
  `).join('');
}

function updateEscrowSimulation(val) {
  const amount = parseFloat(val) || 50;
  const display = document.getElementById('sliderValDisplay');
  if (display) display.textContent = `₹ ${amount.toFixed(0)}`;
  const aid = (amount * 0.90).toFixed(2);
  const ngo = (amount * 0.05).toFixed(2);
  const fee = (amount * 0.05).toFixed(2);
  const aidEl = document.getElementById('simAidNum');
  if (aidEl) aidEl.textContent = `₹ ${aid}`;
  const ngoEl = document.getElementById('simNgoNum');
  if (ngoEl) ngoEl.textContent = `₹ ${ngo}`;
  const feeEl = document.getElementById('simFeeNum');
  if (feeEl) feeEl.textContent = `₹ ${fee}`;
}

// ============================================================
// 10. RENDER DRAWER RECENT DONATIONS
// ============================================================
function renderDrawerDonations() {
  const container = document.getElementById('drawerDonationsList');
  if (!container) return;

  container.innerHTML = userDonationsHistory.slice(0, 3).map(d => `
    <div style="background:var(--bg-subtle); border:1px solid var(--border-hairline); border-radius:var(--radius-xs); padding:10px; margin-bottom:8px; font-size:0.8rem;">
      <div style="display:flex; justify-content:space-between; font-weight:700;">
        <span>${d.causeTitle.substring(0, 24)}...</span>
        <span style="color:var(--emerald);">₹${d.total.toFixed(2)}</span>
      </div>
      <div style="font-size:0.7rem; color:var(--text-muted); margin-top:2px;">
        ${d.date} • Code: <code>${d.id}</code>
      </div>
    </div>
  `).join('');
}

// ============================================================
// 11. DONATION MODAL LOGIC
// ============================================================
function openDonateModal(causeId) {
  const cause = CAUSES_7.find(c => c.id === causeId) || CAUSES_7[0];
  activeCause = cause;

  const titleEl = document.getElementById('modalCauseTitle');
  if (titleEl) titleEl.innerText = `Sponsor: ${cause.title}`;
  const descEl = document.getElementById('modalCauseDesc');
  if (descEl) descEl.innerText = `${cause.desc} Executing NGO: ${cause.ngoName}.`;

  setUnits(1);
  const modal = document.getElementById('donateModal');
  if (modal) modal.classList.remove('hidden');
}

function closeDonateModal() {
  const modal = document.getElementById('donateModal');
  if (modal) modal.classList.add('hidden');
}

function adjustUnits(delta) {
  const input = document.getElementById('donateUnitInput');
  if (!input) return;
  let val = parseInt(input.value, 10) || 1;
  val = Math.max(1, Math.min(100, val + delta));
  input.value = val;
  updateModalTotal();
}

function setUnits(count) {
  const input = document.getElementById('donateUnitInput');
  if (input) input.value = count;
  updateModalTotal();
}

function quickDonate(causeId, count) {
  openDonateModal(causeId);
  setUnits(count);
}

function updateModalTotal() {
  const input = document.getElementById('donateUnitInput');
  const units = input ? parseInt(input.value, 10) || 1 : 1;
  const total = units * activeCause.unitCost;
  const aid = (total * 0.90).toFixed(2);
  const ngo = (total * 0.05).toFixed(2);
  const fee = (total * 0.05).toFixed(2);

  const aidEl = document.getElementById('modalAidSplit');
  if (aidEl) aidEl.innerText = `₹${aid}`;
  const ngoEl = document.getElementById('modalNgoSplit');
  if (ngoEl) ngoEl.innerText = `₹${ngo}`;
  const feeEl = document.getElementById('modalFeeSplit');
  if (feeEl) feeEl.innerText = `₹${fee}`;
  const totalEl = document.getElementById('modalTotalPayable');
  if (totalEl) totalEl.innerText = `₹${total.toFixed(2)}`;
}

function executeMockDonation() {
  const input = document.getElementById('donateUnitInput');
  const units = input ? parseInt(input.value, 10) || 1 : 1;
  const total = units * activeCause.unitCost;
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
    invoiceId: `GST-UP-2026-${randomHex}`,
    status: "Verified & Escrow Locked",
    steps: ["Escrow Locked (UPI)", "Allocated to NGO", "Wholesale Procured", "Live Video Verified", "NTP & GST Audited"]
  });

  closeDonateModal();
  renderProofs();
  renderDrawerDonations();

  // Fire celebratory canvas confetti!
  if (typeof confetti === 'function') {
    confetti({
      particleCount: 110,
      spread: 75,
      origin: { y: 0.6 }
    });
  }

  showToast(`₹${total.toFixed(2)} Authorized! 100% video proof & GST bill linked.`, 'success');
  openSlideover();
}

// ============================================================
// 12. PROOF & INVOICE MODALS
// ============================================================
function openVideoProofModal(txId) {
  const d = userDonationsHistory.find(x => x.id === txId) || userDonationsHistory[0];
  const titleEl = document.getElementById('proofCauseTitle');
  if (titleEl) titleEl.innerText = `${d.causeTitle} — Video Proof`;
  const badgeEl = document.getElementById('proofTxBadge');
  if (badgeEl) badgeEl.innerText = `#${d.id}`;

  const modal = document.getElementById('videoProofModal');
  if (modal) modal.classList.remove('hidden');

  const video = document.getElementById('proofVideoElement');
  if (video) { video.currentTime = 0; video.play().catch(() => {}); }
}

function closeVideoProofModal() {
  const modal = document.getElementById('videoProofModal');
  if (modal) modal.classList.add('hidden');
  const video = document.getElementById('proofVideoElement');
  if (video) video.pause();
}

function openInvoiceModal(invId) {
  const codeEl = document.getElementById('invoiceIdCode');
  if (codeEl) codeEl.innerText = invId || 'GST-UP-2026-8910';
  const modal = document.getElementById('invoiceModal');
  if (modal) modal.classList.remove('hidden');
}

function closeInvoiceModal() {
  const modal = document.getElementById('invoiceModal');
  if (modal) modal.classList.add('hidden');
}

function openCertificateModal() {
  const modal = document.getElementById('certificateModal');
  if (modal) modal.classList.remove('hidden');
}

function closeCertificateModal() {
  const modal = document.getElementById('certificateModal');
  if (modal) modal.classList.add('hidden');
}

function openTaxModal() {
  const modal = document.getElementById('taxModal');
  if (modal) modal.classList.remove('hidden');
}

function closeTaxModal() {
  const modal = document.getElementById('taxModal');
  if (modal) modal.classList.add('hidden');
}

function openSlideover() {
  const drawer = document.getElementById('slideoverBackdrop');
  if (drawer) drawer.classList.add('open');
}

function closeSlideover(e) {
  if (e && e.target && e.target.closest && e.target.closest('.slideover-panel') && e.type === 'click' && !e.target.closest('button')) {
    return;
  }
  const drawer = document.getElementById('slideoverBackdrop');
  if (drawer) drawer.classList.remove('open');
}

// ============================================================
// 13. FIREBASE AUTHENTICATION CONTROLLER
// ============================================================
const firebaseConfig = {
  apiKey: window.__FIREBASE_API_KEY || "AIzaSyDummyKeyForFallbackOffline12345678",
  authDomain: window.__FIREBASE_AUTH_DOMAIN || "acta-resence.firebaseapp.com",
  projectId: window.__FIREBASE_PROJECT_ID || "acta-resence",
  storageBucket: window.__FIREBASE_STORAGE_BUCKET || "acta-resence.appspot.com",
  messagingSenderId: window.__FIREBASE_MESSAGING_SENDER_ID || "1029384756",
  appId: window.__FIREBASE_APP_ID || "1:1029384756:web:abcdef123456"
};

function initFirebaseAuth() {
  if (typeof firebase !== 'undefined' && firebase.apps && !firebase.apps.length) {
    try {
      firebase.initializeApp(firebaseConfig);
    } catch (e) {
      console.warn('[ACTA Auth] Init warning:', e.message);
    }
  }

  if (typeof firebase !== 'undefined' && firebase.auth) {
    try {
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          const name = user.displayName || user.email.split('@')[0] || "Student Donor";
          applySignedInUser(name, user.email || 'student@glbajaj.org');
        }
      });
    } catch (e) {
      console.warn('[ACTA Auth] Auth state listener:', e.message);
    }
  }
}

function openAuthModal() {
  const modal = document.getElementById('authModal');
  if (modal) modal.classList.remove('hidden');
}

function closeAuthModal() {
  const modal = document.getElementById('authModal');
  if (modal) modal.classList.add('hidden');
}

function signInWithGoogle() {
  if (typeof firebase !== 'undefined' && firebase.auth) {
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
      .then((res) => {
        applySignedInUser(res.user.displayName || 'Changemaker', res.user.email);
        closeAuthModal();
      })
      .catch((err) => {
        // Safe alert as requested in code review: do not silently impersonate!
        showToast("Google sign-in offline. Please enter your college email below.", "error");
      });
  } else {
    showToast("Google sign-in offline. Please enter your college email below.", "error");
  }
}

function handleEmailAuthSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById('authEmailInput');
  const email = input && input.value ? input.value : 'student@glbajaj.org';
  const name = email.split('@')[0];
  applySignedInUser(name, email);
  closeAuthModal();
}

function applySignedInUser(name, email) {
  const initials = name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase() || 'ST';
  const navAvatar = document.getElementById('navAvatar');
  if (navAvatar) navAvatar.innerText = initials;
  const navUserName = document.getElementById('navUserName');
  if (navUserName) navUserName.innerText = name.split(' ')[0];

  const authBtn = document.getElementById('navAuthTriggerBtn');
  if (authBtn) authBtn.classList.add('hidden');

  showToast(`Authenticated as ${name} (${email})`, 'success');
  if (typeof confetti === 'function') confetti({ particleCount: 75, spread: 60 });
}

// ============================================================
// 14. SAFE TOAST NOTIFICATIONS (No innerHTML XSS injection)
// ============================================================
function showToast(msg, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  
  const iconSpan = document.createElement('span');
  iconSpan.textContent = type === 'error' ? '⚠️' : '✓';
  iconSpan.style.color = type === 'error' ? 'var(--primary)' : 'var(--emerald)';
  iconSpan.style.fontWeight = 'bold';

  const msgSpan = document.createElement('span');
  msgSpan.textContent = String(msg); // 100% safe from script injection!

  t.appendChild(iconSpan);
  t.appendChild(msgSpan);
  container.appendChild(t);

  setTimeout(() => {
    t.style.opacity = '0';
    setTimeout(() => t.remove(), 250);
  }, 3500);
}

// ============================================================
// 15. INITIALIZATION
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
  render7Causes();
  renderProofs();
  renderXpLadder();
  renderGuilds();
  renderDrawerDonations();
  initFirebaseAuth();
});
