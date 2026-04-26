# Datahack Indonesia Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single `index.html` landing page for Datahack Indonesia that converts visitors into demo bookings via a Formspree-powered contact form.

**Architecture:** Single self-contained `index.html` — all styles via Tailwind CDN + a `<style>` block for custom tokens, Google Fonts via `<link>`, and vanilla JS for the form submission + nav hamburger. No build step, no bundler. Served locally via `node serve.mjs` at `http://localhost:3000`.

**Tech Stack:** HTML5, Tailwind CSS (CDN), Google Fonts (Playfair Display + Public Sans), Vanilla JS, Formspree (free tier)

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `5-website-building/index.html` | Create | Entire landing page — markup, inline styles, JS |
| `5-website-building/brand_assets/Datahack ID Logo.png` | Use (existing) | Logo in nav and footer |

---

### Task 1: HTML Shell + Brand Tokens

**Files:**
- Create: `5-website-building/index.html`

- [ ] **Step 1: Create the HTML shell with all head dependencies**

Create `5-website-building/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Datahack Indonesia — AI-Powered Business Automation</title>
  <meta name="description" content="Datahack Indonesia builds intelligent AI chatbot systems for Indonesian SMEs — automating customer service, converting leads, and delivering deep analytics across WhatsApp, Instagram, Facebook, and TikTok." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;1,700&family=Public+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            'dh-electric': '#3d1ff6',
            'dh-teal': '#099ec3',
            'dh-navy-mid': '#333c70',
            'dh-navy': '#212747',
            'dh-footer': '#1a1f3d',
            'dh-light': '#f8f9fc',
          },
          fontFamily: {
            display: ['Playfair Display', 'Georgia', 'serif'],
            body: ['Public Sans', 'system-ui', 'sans-serif'],
          },
        }
      }
    }
  </script>
  <style>
    * { font-family: 'Public Sans', system-ui, sans-serif; }
    h1, h2, h3, .font-display { font-family: 'Playfair Display', Georgia, serif; }

    /* Grain texture overlay */
    .grain::after {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 1;
    }
    .grain > * { position: relative; z-index: 2; }

    /* Hero gradient */
    .hero-bg {
      background-color: #212747;
      background-image:
        radial-gradient(ellipse 80% 60% at 10% 10%, rgba(9,158,195,0.25) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 90%, rgba(61,31,246,0.30) 0%, transparent 60%);
    }

    /* CTA section gradient */
    .cta-bg {
      background-color: #212747;
      background-image:
        radial-gradient(ellipse 70% 60% at 90% 10%, rgba(9,158,195,0.20) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 10% 90%, rgba(61,31,246,0.28) 0%, transparent 60%);
    }

    /* Card shadow */
    .card-shadow { box-shadow: 0 4px 24px rgba(61,31,246,0.10), 0 1px 4px rgba(0,0,0,0.08); }
    .card-shadow-teal { box-shadow: 0 4px 24px rgba(9,158,195,0.12), 0 1px 4px rgba(0,0,0,0.08); }

    /* Smooth scroll */
    html { scroll-behavior: smooth; }

    /* Button transitions */
    .btn-primary {
      background-color: #3d1ff6;
      color: white;
      transition: background-color 0.2s cubic-bezier(0.34,1.56,0.64,1), transform 0.2s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s ease;
    }
    .btn-primary:hover { background-color: #099ec3; transform: translateY(-1px); box-shadow: 0 8px 24px rgba(61,31,246,0.30); }
    .btn-primary:active { transform: translateY(0); }
    .btn-primary:focus-visible { outline: 2px solid #099ec3; outline-offset: 3px; }

    .btn-ghost {
      color: #099ec3;
      transition: color 0.2s ease, opacity 0.2s ease;
    }
    .btn-ghost:hover { color: #3d1ff6; }
    .btn-ghost:focus-visible { outline: 2px solid #099ec3; outline-offset: 3px; }

    /* Nav link transitions */
    .nav-link {
      color: rgba(255,255,255,0.75);
      transition: color 0.15s ease;
    }
    .nav-link:hover { color: #099ec3; }
    .nav-link:focus-visible { outline: 2px solid #099ec3; outline-offset: 3px; border-radius: 2px; }

    /* Step connector */
    .step-connector {
      flex: 1;
      height: 2px;
      background: repeating-linear-gradient(90deg, #099ec3 0, #099ec3 8px, transparent 8px, transparent 16px);
      margin-top: -1px;
    }

    /* Channel card */
    .channel-card {
      transition: transform 0.2s cubic-bezier(0.34,1.56,0.64,1), background-color 0.2s ease;
    }
    .channel-card:hover { transform: translateY(-3px); background-color: rgba(255,255,255,0.08); }

    /* Form input */
    .form-input {
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px 14px;
      width: 100%;
      font-family: 'Public Sans', sans-serif;
      font-size: 0.9rem;
      color: #212747;
      transition: border-color 0.15s ease, box-shadow 0.15s ease;
      outline: none;
    }
    .form-input:focus { border-color: #3d1ff6; box-shadow: 0 0 0 3px rgba(61,31,246,0.10); }
    .form-input::placeholder { color: #a0aec0; }

    /* Stat card */
    .stat-number {
      font-family: 'Playfair Display', serif;
      font-size: 3rem;
      font-weight: 800;
      color: #3d1ff6;
      line-height: 1;
    }

    /* Hamburger */
    #mobile-menu { display: none; }
    #mobile-menu.open { display: block; }
  </style>
</head>
<body class="bg-white text-gray-800">
  <!-- Sections go here -->
</body>
</html>
```

- [ ] **Step 2: Start the dev server in background**

```bash
cd "c:/Users/ASUS/Documents/Project/7-day-ais-challenge"
node serve.mjs &
```

Expected: server running at `http://localhost:3000`

- [ ] **Step 3: Commit shell**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add html shell with brand tokens and tailwind config"
```

---

### Task 2: Navigation

**Files:**
- Modify: `5-website-building/index.html` — replace `<!-- Sections go here -->` comment, adding nav before it

- [ ] **Step 1: Add the navigation markup inside `<body>` before the sections comment**

```html
<!-- NAV -->
<nav id="nav" class="fixed top-0 left-0 right-0 z-50" style="background: rgba(33,39,71,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255,255,255,0.06);">
  <div class="max-w-7xl mx-auto px-6 flex items-center justify-between h-16">
    <!-- Logo -->
    <a href="#" class="flex items-center gap-2 flex-shrink-0">
      <img src="brand_assets/Datahack ID Logo.png" alt="Datahack Indonesia" class="h-9 w-auto" />
    </a>

    <!-- Desktop links -->
    <div class="hidden md:flex items-center gap-8">
      <a href="#solutions" class="nav-link text-sm font-medium">Solutions</a>
      <a href="#how-it-works" class="nav-link text-sm font-medium">How It Works</a>
      <a href="#results" class="nav-link text-sm font-medium">Results</a>
      <a href="#demo-form" class="nav-link text-sm font-medium">Contact</a>
    </div>

    <!-- CTA + hamburger -->
    <div class="flex items-center gap-4">
      <a href="#demo-form" class="hidden md:inline-flex btn-primary text-sm font-semibold px-5 py-2.5 rounded-full">Book a Demo</a>
      <button id="hamburger" class="md:hidden text-white p-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-dh-teal rounded" aria-label="Toggle menu">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path id="ham-open" stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
          <path id="ham-close" class="hidden" stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>
  </div>

  <!-- Mobile menu -->
  <div id="mobile-menu" class="md:hidden px-6 pb-4 flex flex-col gap-3">
    <a href="#solutions" class="nav-link text-sm font-medium py-1">Solutions</a>
    <a href="#how-it-works" class="nav-link text-sm font-medium py-1">How It Works</a>
    <a href="#results" class="nav-link text-sm font-medium py-1">Results</a>
    <a href="#demo-form" class="nav-link text-sm font-medium py-1">Contact</a>
    <a href="#demo-form" class="btn-primary text-sm font-semibold px-5 py-2.5 rounded-full text-center mt-2">Book a Demo</a>
  </div>
</nav>
```

- [ ] **Step 2: Add hamburger JS before `</body>`**

```html
<script>
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  const hamOpen = document.getElementById('ham-open');
  const hamClose = document.getElementById('ham-close');
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    hamOpen.classList.toggle('hidden');
    hamClose.classList.toggle('hidden');
  });
  // Close on link click
  mobileMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      hamOpen.classList.remove('hidden');
      hamClose.classList.add('hidden');
    });
  });
</script>
```

- [ ] **Step 3: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add fixed navigation with mobile hamburger"
```

---

### Task 3: Hero Section

**Files:**
- Modify: `5-website-building/index.html` — add hero section after nav

- [ ] **Step 1: Add hero markup after the nav closing tag**

```html
<!-- HERO -->
<section class="hero-bg grain relative min-h-screen flex flex-col justify-center pt-16">
  <div class="max-w-7xl mx-auto px-6 py-24 text-center">
    <!-- Eyebrow -->
    <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-6">AI-Powered Business Automation</p>

    <!-- H1 -->
    <h1 class="font-display text-white text-4xl md:text-6xl lg:text-7xl font-bold leading-tight mb-6" style="letter-spacing: -0.03em; max-width: 14ch; margin-left: auto; margin-right: auto;">
      Turn Every Customer Message Into a Business Outcome
    </h1>

    <!-- Subhead -->
    <p class="text-gray-300 text-lg md:text-xl max-w-2xl mx-auto mb-10" style="line-height: 1.7;">
      Datahack Indonesia builds intelligent AI chatbot systems for Indonesian SMEs — automating customer service, converting leads, and delivering deep analytics across WhatsApp, Instagram, Facebook, and TikTok.
    </p>

    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-20">
      <a href="#demo-form" class="btn-primary font-semibold px-8 py-3.5 rounded-full text-base">Book a Free Demo</a>
      <a href="#how-it-works" class="btn-ghost font-medium text-base flex items-center gap-1.5">
        See How It Works
        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
      </a>
    </div>

    <!-- Stats -->
    <div class="flex flex-col sm:flex-row items-center justify-center gap-0 sm:gap-0 divide-y sm:divide-y-0 sm:divide-x divide-white/10">
      <div class="px-8 py-4 text-center">
        <p class="font-display text-dh-electric text-4xl font-bold">5,000+</p>
        <p class="text-gray-400 text-sm mt-1">tickets handled / month</p>
      </div>
      <div class="px-8 py-4 text-center">
        <p class="font-display text-dh-electric text-4xl font-bold">~40%</p>
        <p class="text-gray-400 text-sm mt-1">self-resolution rate</p>
      </div>
      <div class="px-8 py-4 text-center">
        <p class="font-display text-dh-electric text-4xl font-bold">200+</p>
        <p class="text-gray-400 text-sm mt-1">customers onboarded / month</p>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Screenshot and verify**

```bash
node screenshot.mjs http://localhost:3000 hero
```

Read the screenshot from `5-website-building/temporary screenshots/` and verify: dark navy background, teal/blue gradient glows, large Playfair heading, 3 stats with electric blue numbers.

- [ ] **Step 3: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add hero section with stats row"
```

---

### Task 4: Problem Section

**Files:**
- Modify: `5-website-building/index.html` — add after hero section

- [ ] **Step 1: Add problem section markup**

```html
<!-- PROBLEM -->
<section id="solutions" class="bg-dh-light py-24">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-center mb-16">
      <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-3">The Problem</p>
      <h2 class="font-display text-dh-navy text-3xl md:text-5xl font-bold" style="letter-spacing: -0.03em;">Your Team Shouldn't Be<br/>Doing This Manually</h2>
    </div>

    <div class="grid md:grid-cols-2 gap-8 mb-16">
      <!-- Pain card 1 -->
      <div class="bg-white rounded-2xl p-8 card-shadow-teal">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background: rgba(9,158,195,0.10);">
          <svg class="w-6 h-6 text-dh-teal" fill="none" stroke="#099ec3" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        </div>
        <h3 class="font-display text-dh-navy text-xl font-bold mb-4">Drowning in Repetitive Tickets</h3>
        <ul class="space-y-3">
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal mt-0.5 flex-shrink-0">✕</span>Hundreds of identical questions every day</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal mt-0.5 flex-shrink-0">✕</span>Slow response times → unhappy customers</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal mt-0.5 flex-shrink-0">✕</span>Agents burn out on work that doesn't need a human</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal mt-0.5 flex-shrink-0">✕</span>Inconsistent answers damage your brand</li>
        </ul>
      </div>

      <!-- Pain card 2 -->
      <div class="bg-white rounded-2xl p-8 card-shadow-teal">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background: rgba(61,31,246,0.08);">
          <svg class="w-6 h-6" fill="none" stroke="#3d1ff6" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        </div>
        <h3 class="font-display text-dh-navy text-xl font-bold mb-4">Leads Going Cold While You Sleep</h3>
        <ul class="space-y-3">
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric mt-0.5 flex-shrink-0">✕</span>High inbound volume across 4+ channels</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric mt-0.5 flex-shrink-0">✕</span>No one following up on warm leads</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric mt-0.5 flex-shrink-0">✕</span>Manual stock and price checking slows replies</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric mt-0.5 flex-shrink-0">✕</span>Potential customers bought from a faster competitor</li>
        </ul>
      </div>
    </div>

    <!-- Pull quote -->
    <blockquote class="text-center max-w-3xl mx-auto">
      <p class="font-display text-dh-navy text-2xl md:text-3xl italic" style="line-height:1.5;">"The problem isn't your team. It's the lack of intelligent automation."</p>
    </blockquote>
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add problem section with pain cards and pull quote"
```

---

### Task 5: Solution Section

**Files:**
- Modify: `5-website-building/index.html` — add after problem section

- [ ] **Step 1: Add solution section markup**

```html
<!-- SOLUTION -->
<section class="bg-white py-24">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-center mb-16">
      <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-3">The Solution</p>
      <h2 class="font-display text-dh-navy text-3xl md:text-5xl font-bold mb-4" style="letter-spacing:-0.03em;">Two AI Systems. One Unified Platform.</h2>
      <p class="text-gray-500 text-base max-w-xl mx-auto">Built on RAG architecture, multi-agent design, and omnichannel integration.</p>
    </div>

    <div class="grid md:grid-cols-2 gap-8">
      <!-- Customer Service AI -->
      <div class="rounded-2xl overflow-hidden card-shadow flex flex-col">
        <div class="h-1.5 bg-dh-teal"></div>
        <div class="p-8 flex flex-col flex-1">
          <span class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-3">Customer Service AI</span>
          <h3 class="font-display text-dh-navy text-2xl font-bold mb-3">24/7 Intelligent Support</h3>
          <p class="text-gray-600 text-sm mb-6" style="line-height:1.7;">An AI system that reads, understands, and resolves customer messages automatically — across all your channels. It handles troubleshooting, reads images sent by customers, escalates when needed, and classifies every ticket automatically.</p>
          <ul class="space-y-2.5 mt-auto">
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(9,158,195,0.12);">✓</span>RAG Knowledge Base</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(9,158,195,0.12);">✓</span>Image Understanding</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(9,158,195,0.12);">✓</span>Human Escalation</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(9,158,195,0.12);">✓</span>Auto-Classification</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(9,158,195,0.12);">✓</span>Follow-Up Automation</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(9,158,195,0.12);">✓</span>Multi-Channel</li>
          </ul>
        </div>
      </div>

      <!-- Lead Conversion AI -->
      <div class="rounded-2xl overflow-hidden card-shadow flex flex-col">
        <div class="h-1.5 bg-dh-electric"></div>
        <div class="p-8 flex flex-col flex-1">
          <span class="text-dh-electric text-xs font-semibold uppercase tracking-widest mb-3">Lead Conversion AI</span>
          <h3 class="font-display text-dh-navy text-2xl font-bold mb-3">Always-On Sales Agent</h3>
          <p class="text-gray-600 text-sm mb-6" style="line-height:1.7;">An AI that engages every inbound lead, answers product questions, checks live inventory, and moves prospects toward booking — automatically, across WhatsApp, Instagram, Facebook, and TikTok.</p>
          <ul class="space-y-2.5 mt-auto">
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(61,31,246,0.10);">✓</span>RAG Product Knowledge</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(61,31,246,0.10);">✓</span>Live Inventory Check</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(61,31,246,0.10);">✓</span>Lead Qualification</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(61,31,246,0.10);">✓</span>Proactive Follow-Up</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(61,31,246,0.10);">✓</span>Auto-Classification</li>
            <li class="flex items-center gap-2.5 text-sm text-gray-700"><span class="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style="background:rgba(61,31,246,0.10);">✓</span>4 Channels</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add solution section with two AI system cards"
```

---

### Task 6: How It Works Section

**Files:**
- Modify: `5-website-building/index.html` — add after solution section

- [ ] **Step 1: Add how it works markup**

```html
<!-- HOW IT WORKS -->
<section id="how-it-works" class="bg-dh-light py-24">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-center mb-16">
      <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-3">How It Works</p>
      <h2 class="font-display text-dh-navy text-3xl md:text-5xl font-bold" style="letter-spacing:-0.03em;">From Message to Outcome<br/>in Seconds</h2>
    </div>

    <!-- 5-step flow -->
    <div class="flex flex-col md:flex-row items-start md:items-center gap-0 mb-16">
      <!-- Step 1 -->
      <div class="flex flex-col items-center text-center md:w-1/5 px-2 py-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg mb-3 flex-shrink-0" style="background:#3d1ff6;">1</div>
        <p class="font-semibold text-dh-navy text-sm mb-1">Customer Sends Message</p>
        <p class="text-gray-500 text-xs" style="line-height:1.6;">On any channel: WhatsApp, Instagram, Facebook, or TikTok</p>
      </div>
      <div class="step-connector hidden md:block"></div>
      <!-- Step 2 -->
      <div class="flex flex-col items-center text-center md:w-1/5 px-2 py-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg mb-3 flex-shrink-0" style="background:#3d1ff6;">2</div>
        <p class="font-semibold text-dh-navy text-sm mb-1">Message Reaches Your AI</p>
        <p class="text-gray-500 text-xs" style="line-height:1.6;">Via unified omnichannel integration</p>
      </div>
      <div class="step-connector hidden md:block"></div>
      <!-- Step 3 -->
      <div class="flex flex-col items-center text-center md:w-1/5 px-2 py-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg mb-3 flex-shrink-0" style="background:#3d1ff6;">3</div>
        <p class="font-semibold text-dh-navy text-sm mb-1">AI Retrieves Knowledge</p>
        <p class="text-gray-500 text-xs" style="line-height:1.6;">Fetches relevant knowledge &amp; conversation history</p>
      </div>
      <div class="step-connector hidden md:block"></div>
      <!-- Step 4 -->
      <div class="flex flex-col items-center text-center md:w-1/5 px-2 py-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg mb-3 flex-shrink-0" style="background:#3d1ff6;">4</div>
        <p class="font-semibold text-dh-navy text-sm mb-1">Agent Responds or Escalates</p>
        <p class="text-gray-500 text-xs" style="line-height:1.6;">Responds intelligently or routes to human when needed</p>
      </div>
      <div class="step-connector hidden md:block"></div>
      <!-- Step 5 -->
      <div class="flex flex-col items-center text-center md:w-1/5 px-2 py-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg mb-3 flex-shrink-0" style="background:#099ec3;">5</div>
        <p class="font-semibold text-dh-navy text-sm mb-1">Outcome Delivered</p>
        <p class="text-gray-500 text-xs" style="line-height:1.6;">Resolved, converted, or followed up — every time</p>
      </div>
    </div>

    <!-- Agent cards 2x2 -->
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-white rounded-xl p-6 card-shadow">
        <div class="w-10 h-10 rounded-lg flex items-center justify-center mb-4" style="background:rgba(9,158,195,0.10);">
          <svg class="w-5 h-5" fill="none" stroke="#099ec3" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
        </div>
        <h4 class="font-display text-dh-navy font-bold text-base mb-1">Answer Agent</h4>
        <p class="text-gray-500 text-xs mb-3" style="line-height:1.6;">Core RAG agent: retrieves relevant knowledge, injects conversation history, generates a response.</p>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-full" style="background:rgba(9,158,195,0.10);color:#099ec3;">All Systems</span>
      </div>
      <div class="bg-white rounded-xl p-6 card-shadow">
        <div class="w-10 h-10 rounded-lg flex items-center justify-center mb-4" style="background:rgba(61,31,246,0.08);">
          <svg class="w-5 h-5" fill="none" stroke="#3d1ff6" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
        </div>
        <h4 class="font-display text-dh-navy font-bold text-base mb-1">Escalation &amp; Oversight Agent</h4>
        <p class="text-gray-500 text-xs mb-3" style="line-height:1.6;">Monitors conversations, triggers human handoff when needed, allows manual override at any time.</p>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-full" style="background:rgba(61,31,246,0.08);color:#3d1ff6;">All Systems</span>
      </div>
      <div class="bg-white rounded-xl p-6 card-shadow">
        <div class="w-10 h-10 rounded-lg flex items-center justify-center mb-4" style="background:rgba(9,158,195,0.10);">
          <svg class="w-5 h-5" fill="none" stroke="#099ec3" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
        </div>
        <h4 class="font-display text-dh-navy font-bold text-base mb-1">Follow-Up &amp; Classification Agent</h4>
        <p class="text-gray-500 text-xs mb-3" style="line-height:1.6;">Proactively follows up on unresolved conversations, auto-tags and closes tickets.</p>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-full" style="background:rgba(9,158,195,0.10);color:#099ec3;">All Systems</span>
      </div>
      <div class="bg-white rounded-xl p-6 card-shadow">
        <div class="w-10 h-10 rounded-lg flex items-center justify-center mb-4" style="background:rgba(61,31,246,0.08);">
          <svg class="w-5 h-5" fill="none" stroke="#3d1ff6" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
        </div>
        <h4 class="font-display text-dh-navy font-bold text-base mb-1">Image Processing Agent</h4>
        <p class="text-gray-500 text-xs mb-3" style="line-height:1.6;">Classifies and reads customer-submitted images: receipts, product photos, error screens, and more.</p>
        <span class="text-xs font-semibold px-2 py-0.5 rounded-full" style="background:rgba(61,31,246,0.08);color:#3d1ff6;">Customer Service AI</span>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add how it works section with steps and agent cards"
```

---

### Task 7: Omnichannel Strip + Results Section

**Files:**
- Modify: `5-website-building/index.html` — add after how-it-works section

- [ ] **Step 1: Add omnichannel strip**

```html
<!-- OMNICHANNEL STRIP -->
<section style="background:#212747;">
  <div class="max-w-7xl mx-auto px-6 py-16">
    <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest text-center mb-10">Omnichannel</p>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-12">
      <div class="channel-card rounded-xl p-6 text-center" style="background:rgba(255,255,255,0.05);">
        <div class="text-3xl mb-3">💬</div>
        <h4 class="text-white font-semibold text-sm mb-1">WhatsApp</h4>
        <p class="text-gray-400 text-xs" style="line-height:1.6;">Highest volume support &amp; sales channel — where your customers already are.</p>
      </div>
      <div class="channel-card rounded-xl p-6 text-center" style="background:rgba(255,255,255,0.05);">
        <div class="text-3xl mb-3">📸</div>
        <h4 class="text-white font-semibold text-sm mb-1">Instagram</h4>
        <p class="text-gray-400 text-xs" style="line-height:1.6;">DM automation for social leads &amp; complaints — close the loop instantly.</p>
      </div>
      <div class="channel-card rounded-xl p-6 text-center" style="background:rgba(255,255,255,0.05);">
        <div class="text-3xl mb-3">👥</div>
        <h4 class="text-white font-semibold text-sm mb-1">Facebook</h4>
        <p class="text-gray-400 text-xs" style="line-height:1.6;">Community and campaign lead capture — turn followers into customers.</p>
      </div>
      <div class="channel-card rounded-xl p-6 text-center" style="background:rgba(255,255,255,0.05);">
        <div class="text-3xl mb-3">🎵</div>
        <h4 class="text-white font-semibold text-sm mb-1">TikTok</h4>
        <p class="text-gray-400 text-xs" style="line-height:1.6;">Organic and paid lead conversion — capture intent the moment it strikes.</p>
      </div>
    </div>
    <blockquote class="text-center max-w-2xl mx-auto">
      <p class="font-display text-dh-teal text-xl md:text-2xl italic" style="line-height:1.5;">"All channels feed into one unified AI brain. One knowledge base. One conversation history. One analytics view."</p>
    </blockquote>
  </div>
</section>

<!-- RESULTS -->
<section id="results" class="bg-white py-24">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-center mb-16">
      <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-3">Results</p>
      <h2 class="font-display text-dh-navy text-3xl md:text-5xl font-bold" style="letter-spacing:-0.03em;">Built and Proven in Production</h2>
    </div>

    <!-- Stat cards -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
      <div class="rounded-2xl p-8 text-center card-shadow">
        <p class="stat-number">5,000+</p>
        <p class="text-gray-500 text-sm mt-2">tickets/month handled by AI</p>
      </div>
      <div class="rounded-2xl p-8 text-center card-shadow">
        <p class="stat-number">~40%</p>
        <p class="text-gray-500 text-sm mt-2">self-resolution, no human needed</p>
      </div>
      <div class="rounded-2xl p-8 text-center card-shadow">
        <p class="stat-number">~333</p>
        <p class="text-gray-500 text-sm mt-2">hours/month CS labor saved</p>
      </div>
      <div class="rounded-2xl p-8 text-center card-shadow">
        <p class="stat-number">200+</p>
        <p class="text-gray-500 text-sm mt-2">customers/month onboarded via AI</p>
      </div>
    </div>

    <!-- Two column benefits -->
    <div class="grid md:grid-cols-2 gap-12">
      <div>
        <h3 class="font-display text-dh-navy text-xl font-bold mb-5">Tangible Results</h3>
        <ul class="space-y-3">
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal font-bold mt-0.5 flex-shrink-0">→</span>~2,000 tickets/month deflected from human agents</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal font-bold mt-0.5 flex-shrink-0">→</span>333 hours/month of manual work eliminated</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal font-bold mt-0.5 flex-shrink-0">→</span>200 customers onboarded monthly through automated sales flow</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-teal font-bold mt-0.5 flex-shrink-0">→</span>4% conversion rate on inbound leads</li>
        </ul>
      </div>
      <div>
        <h3 class="font-display text-dh-navy text-xl font-bold mb-5">Intangible Benefits</h3>
        <ul class="space-y-3">
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric font-bold mt-0.5 flex-shrink-0">→</span>Consistent, always-accurate responses 24/7</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric font-bold mt-0.5 flex-shrink-0">→</span>Reduced agent burnout on repetitive queries</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric font-bold mt-0.5 flex-shrink-0">→</span>Faster lead response → lower drop-off</li>
          <li class="flex items-start gap-3 text-gray-600 text-sm" style="line-height:1.7;"><span class="text-dh-electric font-bold mt-0.5 flex-shrink-0">→</span>Scalable: handles 2× volume without adding headcount</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add omnichannel strip and results section"
```

---

### Task 8: CTA Form Section

**Files:**
- Modify: `5-website-building/index.html` — add after results section

- [ ] **Step 1: Add the CTA form section**

```html
<!-- CTA FORM -->
<section id="demo-form" class="cta-bg grain relative py-24">
  <div class="max-w-3xl mx-auto px-6 text-center">
    <p class="text-dh-teal text-xs font-semibold uppercase tracking-widest mb-4">Get Started</p>
    <h2 class="font-display text-white text-3xl md:text-5xl font-bold mb-4" style="letter-spacing:-0.03em;">Ready to Automate<br/>Your Business?</h2>
    <p class="text-gray-300 text-base mb-8" style="line-height:1.7;">Book a free 30-minute demo and we'll show you exactly how the system works for your business.</p>

    <!-- Trust badges -->
    <div class="flex flex-wrap items-center justify-center gap-6 mb-10">
      <span class="flex items-center gap-2 text-gray-300 text-sm"><span>🔒</span>Your data stays private</span>
      <span class="flex items-center gap-2 text-gray-300 text-sm"><span>🇮🇩</span>Built for Indonesian businesses</span>
      <span class="flex items-center gap-2 text-gray-300 text-sm"><span>⚡</span>Setup in days, not months</span>
    </div>

    <!-- Form card -->
    <div id="form-card" class="bg-white rounded-2xl p-8 md:p-10 text-left" style="box-shadow:0 24px 64px rgba(0,0,0,0.25);">
      <form id="demo-form-el" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
        <div class="grid sm:grid-cols-2 gap-5 mb-5">
          <div>
            <label class="block text-xs font-semibold text-dh-navy mb-1.5 uppercase tracking-wide">Name</label>
            <input type="text" name="name" required placeholder="Your full name" class="form-input" />
          </div>
          <div>
            <label class="block text-xs font-semibold text-dh-navy mb-1.5 uppercase tracking-wide">Business Name</label>
            <input type="text" name="business_name" required placeholder="Your business name" class="form-input" />
          </div>
          <div>
            <label class="block text-xs font-semibold text-dh-navy mb-1.5 uppercase tracking-wide">WhatsApp Number</label>
            <input type="tel" name="whatsapp" required placeholder="+62 8xx xxxx xxxx" class="form-input" />
          </div>
          <div>
            <label class="block text-xs font-semibold text-dh-navy mb-1.5 uppercase tracking-wide">What are you looking for?</label>
            <select name="intent" required class="form-input" style="background:white;">
              <option value="" disabled selected>Select an option...</option>
              <option value="customer-service">Customer Service Automation</option>
              <option value="lead-conversion">Lead Conversion AI</option>
              <option value="both">Both Systems</option>
              <option value="not-sure">Not Sure Yet</option>
            </select>
          </div>
          <div class="sm:col-span-2">
            <label class="block text-xs font-semibold text-dh-navy mb-1.5 uppercase tracking-wide">Estimated messages / tickets per month</label>
            <select name="volume" required class="form-input" style="background:white;">
              <option value="" disabled selected>Select a range...</option>
              <option value="under-500">Under 500</option>
              <option value="500-2000">500 – 2,000</option>
              <option value="2000-5000">2,000 – 5,000</option>
              <option value="5000-plus">5,000+</option>
            </select>
          </div>
        </div>
        <div class="mb-6">
          <label class="block text-xs font-semibold text-dh-navy mb-1.5 uppercase tracking-wide">Message (optional)</label>
          <textarea name="message" rows="4" placeholder="Tell us about your business and current challenges..." class="form-input resize-none"></textarea>
        </div>
        <button type="submit" id="submit-btn" class="btn-primary w-full py-4 rounded-xl font-bold text-base">Book My Free Demo</button>
      </form>
    </div>

    <!-- Thank you state (hidden initially) -->
    <div id="thank-you-card" class="hidden bg-white rounded-2xl p-10 text-center" style="box-shadow:0 24px 64px rgba(0,0,0,0.25);">
      <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-5" style="background:rgba(9,158,195,0.12);">
        <svg class="w-8 h-8" fill="none" stroke="#099ec3" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
      </div>
      <h3 class="font-display text-dh-navy text-2xl font-bold mb-2">We'll be in touch!</h3>
      <p class="text-gray-500" style="line-height:1.7;">Thanks for reaching out. We'll contact you via WhatsApp within 24 hours to schedule your free demo.</p>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Add form submission JS (append to the existing `<script>` block before `</body>`)**

```js
  // Form submission
  const formEl = document.getElementById('demo-form-el');
  const submitBtn = document.getElementById('submit-btn');
  const formCard = document.getElementById('form-card');
  const thankYouCard = document.getElementById('thank-you-card');

  if (formEl) {
    formEl.addEventListener('submit', async (e) => {
      e.preventDefault();
      submitBtn.textContent = 'Sending...';
      submitBtn.disabled = true;

      try {
        const res = await fetch(formEl.action, {
          method: 'POST',
          body: new FormData(formEl),
          headers: { 'Accept': 'application/json' }
        });
        if (res.ok) {
          formCard.classList.add('hidden');
          thankYouCard.classList.remove('hidden');
        } else {
          submitBtn.textContent = 'Something went wrong. Try again.';
          submitBtn.disabled = false;
        }
      } catch {
        submitBtn.textContent = 'Something went wrong. Try again.';
        submitBtn.disabled = false;
      }
    });
  }
```

- [ ] **Step 3: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add CTA demo form with Formspree integration and thank-you state"
```

---

### Task 9: Footer

**Files:**
- Modify: `5-website-building/index.html` — add after CTA form section, before `</body>`

- [ ] **Step 1: Add footer markup**

```html
<!-- FOOTER -->
<footer style="background:#1a1f3d;">
  <div class="max-w-7xl mx-auto px-6 py-12">
    <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-8 mb-8 pb-8" style="border-bottom:1px solid rgba(255,255,255,0.08);">
      <!-- Logo + tagline -->
      <div>
        <img src="brand_assets/Datahack ID Logo.png" alt="Datahack Indonesia" class="h-10 w-auto mb-2" />
        <p class="text-gray-400 text-sm">Intelligent automation for Indonesian SMEs</p>
      </div>
      <!-- Nav -->
      <nav class="flex flex-wrap gap-6">
        <a href="#solutions" class="text-gray-400 hover:text-dh-teal text-sm transition-colors duration-150">Solutions</a>
        <a href="#how-it-works" class="text-gray-400 hover:text-dh-teal text-sm transition-colors duration-150">How It Works</a>
        <a href="#results" class="text-gray-400 hover:text-dh-teal text-sm transition-colors duration-150">Results</a>
        <a href="#demo-form" class="text-gray-400 hover:text-dh-teal text-sm transition-colors duration-150">Contact</a>
      </nav>
      <!-- Email -->
      <a href="mailto:datahackindonesia@gmail.com" class="text-gray-400 hover:text-dh-teal text-sm transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-dh-teal rounded">datahackindonesia@gmail.com</a>
    </div>
    <p class="text-center text-gray-500 text-xs">© 2025 Datahack Indonesia. All rights reserved.</p>
  </div>
</footer>
```

- [ ] **Step 2: Commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): add footer with logo, nav, and email"
```

---

### Task 10: Screenshot Review + Polish Pass

**Files:**
- Modify: `5-website-building/index.html` — fix any visual issues found

- [ ] **Step 1: Take full-page screenshot**

```bash
node screenshot.mjs http://localhost:3000 full
```

Read the screenshot. Check: nav fixed and correct colors, hero gradient visible, stats aligned, section spacing consistent, cards have shadows, footer dark and clean.

- [ ] **Step 2: Invoke frontend-design skill**

Before making any polish fixes, invoke the `frontend-design` skill to guide the review pass.

- [ ] **Step 3: Take a second screenshot after fixes**

```bash
node screenshot.mjs http://localhost:3000 final
```

Read and compare to the first screenshot. Confirm all issues from Step 1 are resolved.

- [ ] **Step 4: Final commit**

```bash
git add 5-website-building/index.html
git commit -m "feat(day5): polish pass - spacing, typography, and visual consistency fixes"
```

---

## Self-Review

**Spec coverage check:**
- ✅ Nav with logo, links, CTA button → Task 2
- ✅ Hero with gradient, eyebrow, H1, subhead, dual CTA, stats → Task 3
- ✅ Problem section with 2 pain cards + pull quote → Task 4
- ✅ Solution section with 2 AI system cards → Task 5
- ✅ How It Works 5-step flow + 4 agent cards → Task 6
- ✅ Omnichannel strip + Results with stats + benefits lists → Task 7
- ✅ CTA form with Formspree, trust badges, thank-you state → Task 8
- ✅ Footer → Task 9
- ✅ Brand tokens (colors, fonts) → Task 1
- ✅ Mobile responsive (Tailwind md: breakpoints throughout)
- ✅ Hamburger nav → Task 2
- ✅ Frontend-design skill invoked → Task 10

**Placeholder scan:** Formspree ID placeholder `YOUR_FORM_ID` is intentional and documented — user must replace after signing up at formspree.io. No other TBDs.

**Type consistency:** All IDs (`demo-form`, `form-card`, `thank-you-card`, `submit-btn`, `demo-form-el`) are consistent between HTML and JS across Tasks 8.
