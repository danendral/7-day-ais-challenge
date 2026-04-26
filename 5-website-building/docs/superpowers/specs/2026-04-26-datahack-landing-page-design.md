# Datahack Indonesia Landing Page — Design Spec
Date: 2026-04-26

## Overview
A single-page marketing landing page for Datahack Indonesia, an end-to-end AI automation company targeting Indonesian SMEs. Primary goal: convert visitors into demo bookings. Single `index.html`, all styles inline, Tailwind CSS via CDN.

## Brand Tokens
| Token | Value |
|---|---|
| Electric Blue | `#3d1ff6` |
| Teal | `#099ec3` |
| Navy Mid | `#333c70` |
| Dark Navy | `#212747` |
| Footer Navy | `#1a1f3d` |
| Heading Font | Playfair Display (Google Fonts) |
| Body Font | Public Sans (Google Fonts) |
| Logo | `brand_assets/Datahack ID Logo.png` |

## Visual System
- **Background treatment:** Layered radial gradients — dark navy base with teal glow top-left/right and electric blue glow bottom-right/left. SVG grain/noise texture overlay at low opacity for depth.
- **Shadows:** Layered, color-tinted (never flat `shadow-md`). Elevated cards use `0 4px 24px rgba(61,31,246,0.10), 0 1px 4px rgba(0,0,0,0.08)`.
- **Typography:** Playfair Display for all headings, tight tracking (`-0.03em`). Public Sans for body, `line-height: 1.7`.
- **Animations:** Only `transform` and `opacity`. Spring-style easing (`cubic-bezier(0.34,1.56,0.64,1)`). No `transition-all`.
- **Interactive states:** Every clickable element has hover, focus-visible, and active states.
- **Depth layers:** Base (`#f8f9fc`) → Elevated (white card) → Floating (nav, modal).

## Page Structure

### 1. Navigation (fixed)
- Background: `#212747` with `backdrop-filter: blur(12px)`, slight transparency
- Left: Logo PNG
- Center: Links — Solutions, How It Works, Results, Contact
- Right: "Book a Demo" CTA button → anchors to `#demo-form`
- Button: electric blue bg, teal hover, white text, rounded-full

### 2. Hero (full-viewport, dark)
- Background: dark navy + layered radial gradients (teal top-left, electric blue bottom-right) + grain texture
- Eyebrow: `AI-POWERED BUSINESS AUTOMATION` — teal, small-caps, wide tracking
- H1 (Playfair Display, large, white, tight tracking): "Turn Every Customer Message Into a Business Outcome"
- Subhead (Public Sans, gray-300): one-sentence company description
- Primary CTA: "Book a Free Demo" → `#demo-form`, electric blue button
- Secondary link: "See How It Works ↓" — text link, teal, smooth scroll
- Stats row: 3 metrics (5,000+ tickets/month | ~40% self-resolution | 200+ customers/month) — numbers in electric blue Playfair, labels in gray, separated by vertical dividers

### 3. Problem Section (light, `#f8f9fc`)
- Section title (Playfair, dark navy): "Your Team Shouldn't Be Doing This Manually"
- Two pain cards side by side: "Drowning in Repetitive Tickets" + "Leads Going Cold While You Sleep"
- Each card: icon, bold subheading, 4 bullet points, teal-tinted shadow
- Full-width pull quote (italic Playfair, centered, dark navy): "The problem isn't your team. It's the lack of intelligent automation."

### 4. Solution Section (white)
- Section title (Playfair, centered): "Two AI Systems. One Unified Platform."
- Subtitle: "Built on RAG architecture, multi-agent design, and omnichannel integration."
- Two feature cards side by side:
  - **Customer Service AI** — teal top accent bar, 6 feature bullets with checkmarks
  - **Lead Conversion AI** — electric blue top accent bar, 6 feature bullets with checkmarks
- Cards: white, elevated shadow, rounded-2xl

### 5. How It Works (light, `#f8f9fc`)
- Section title: "From Message to Outcome in Seconds"
- 5-step horizontal flow (desktop) / vertical stack (mobile): numbered circle (electric blue), step title, one-line description, dashed connector arrows between steps
- Steps: Customer Sends Message → Message Reaches AI → AI Retrieves Knowledge → Agent Responds or Escalates → Outcome Delivered
- 2×2 agent card grid below: Answer Agent, Escalation Agent, Follow-Up Agent, Image Processing Agent — each with icon, name, description, system badge

### 6. Omnichannel Strip (dark navy band)
- Full-width, `#212747` background
- 4 channel blocks: WhatsApp, Instagram, Facebook, TikTok — icon + name + one-liner
- Pull quote centered below in teal italic: "All channels feed into one unified AI brain. One knowledge base. One conversation history. One analytics view."

### 7. Results (white)
- Section title: "Built and Proven in Production"
- 4 large stat cards in a row: 5,000+ tickets/month | ~40% self-resolution | ~333 hrs saved/month | 200+ customers/month — numbers in Playfair Display, electric blue, oversized
- Two-column list below: Tangible Results (4 bullets) + Intangible Benefits (4 bullets)

### 8. CTA Form / Demo Section (dark, `#demo-form`)
- Background: same radial gradient treatment as hero (teal + electric blue glows + grain)
- Centered heading (Playfair, white): "Ready to Automate Your Business?"
- Subtext (Public Sans, gray-300)
- 3 trust badges inline: lock icon "Your data stays private" | flag icon "Built for Indonesian businesses" | lightning icon "Setup in days, not months"
- White floating form card (elevated shadow):
  - 2-col grid: Name, Business Name, WhatsApp Number, "What are you looking for?" (select), "Estimated messages/month" (select)
  - Full-width: Message textarea
  - Full-width submit: "Book My Free Demo" — electric blue, bold
- Form action: `https://formspree.io/f/YOUR_FORM_ID` (POST), method=POST, AJAX redirect to thank-you state
- On success: swap form card for a thank-you message (green checkmark, "We'll be in touch within 24 hours")

### 9. Footer (`#1a1f3d`)
- Logo + tagline left: "Intelligent automation for Indonesian SMEs"
- Nav links center: Solutions, How It Works, Results, Contact
- Email right: datahackindonesia@gmail.com
- Bottom bar: "© 2025 Datahack Indonesia. All rights reserved." centered

## Responsive Behavior
- Mobile-first. All multi-column layouts collapse to single column below `md` (768px).
- Nav collapses to hamburger menu on mobile with slide-down drawer.
- Stats row stacks 1-col on mobile.
- How It Works steps stack vertically with connector arrows replaced by vertical line.

## Form Submission
- Method: POST to Formspree (`https://formspree.io/f/YOUR_FORM_ID`)
- Fields: name, business_name, whatsapp, intent (select), volume (select), message
- JS intercepts submit, shows loading state on button, on success replaces form with thank-you card
- No backend required beyond Formspree free tier

## File Output
- Single `5-website-building/index.html`
- All CSS inline via Tailwind CDN + `<style>` block for custom tokens
- Google Fonts loaded via `<link>`
- Logo referenced as relative path: `brand_assets/Datahack ID Logo.png`
