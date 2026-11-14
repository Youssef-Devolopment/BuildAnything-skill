---
name: Website
description: Build websites — landing pages, marketing sites, static sites, and docs sites — with real content, strong SEO, and top performance scores. Load when the project is a website or a page-heavy project, or when work involves copy, meta tags, sitemaps, or Core Web Vitals. Follows build-anything's stage gates and design-ui's visual decisions.
---

# Website

Load `build-anything` first (discovery, plan, stage gates) and `design-ui` for visual decisions. This skill covers websites whose product *is* the content and the impression.

## Process (in order)

1. **Content first** — get or write the real copy before layout: headline, subhead, proof (numbers, testimonials, logos), CTA, FAQ. A design without real words is decoration. Never ship lorem ipsum.
2. **Structure** — sitemap + section outline of each page (hero → problem → solution → proof → features → pricing/FAQ → CTA). One primary CTA per page, repeated at natural points.
3. **Design** — apply `design-ui` decisions; mobile-first, since most traffic is mobile.
4. **Build** — static-first (see stack); every page reachable in ≤2 clicks; internal links valid.
5. **Audit before the stage gate** — Lighthouse/performance, SEO, links, breakpoints (see quality bar).

## Stack (defaults — record in `PLAN.md`)

- **Astro** for content/marketing sites (zero JS by default, ships HTML) or **Next.js** if it must grow into an app.
- Tailwind CSS; MDX for content pages; no client framework where HTML + a little JS does the job.
- Forms: server endpoint or a provider (Formspree/Resend) with spam protection (honeypot or Turnstile).

## Quality bar

- **Performance**: Lighthouse ≥95 performance/a11y/SEO; Core Web Vitals green (LCP <2.5s, CLS <0.1, INP <200ms); images `srcset` + explicit dimensions + lazy below fold; self-hosted/minimal fonts; no third-party script that costs >100ms without justification.
- **Effects budget**: animation/3D decoration is *encouraged* on landing/marketing pages (pick a tier from `design-ui`'s ladder) — but it must survive the numbers above. Effect code ≤ ~50KB gzipped, nothing delays LCP or blocks input, content fully readable before/without effects. If an effect drops a score below the bar, shrink or cut it — the score is non-negotiable, the decoration is not. State at review what you added and why.
- **SEO**: unique title + meta description per page; one `h1`; semantic heading order; Open Graph + Twitter card images; `sitemap.xml` + `robots.txt`; canonical URLs; JSON-LD structured data where it fits (Organization, Product, FAQ).
- **Accessibility**: WCAG AA contrast, keyboard-navigable, visible focus, alt text, landmarks.
- **Responsive**: real content at 320/768/1024/1440px; no overflow; touch targets ≥44px.
- **Trust details**: no broken links, no placeholder testimonials/prices, 404 page, favicon, `og:image`, working analytics (privacy-friendly: Plausible/Fathom over cookie-heavy trackers).

## Testing

- Link checker (internal + external) and HTML validation.
- Lighthouse CI (or manual run) recorded per stage.
- Visual check at all breakpoints in a real browser — including with real copy lengths.

## Rules

- Every number, testimonial, and claim on the page must be real or explicitly flagged by the user as placeholder.
- No JS framework on a page that doesn't need it.
- If analytics/consent requirements are unclear (EU traffic), ask in discovery.
