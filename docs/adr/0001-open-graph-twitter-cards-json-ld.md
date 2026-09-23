# ADR 0001: Open Graph, Twitter Cards, and JSON-LD for Social Link Previews

## Status
Accepted

## Context
The portfolio website (aria-aramesh.ir) currently displays raw URLs when shared on social platforms (Telegram, WhatsApp, Discord, Facebook, LinkedIn, X/Twitter). No Open Graph tags, Twitter Card metadata, or structured data exist.

## Decision
Implement comprehensive social link preview support:

1. **Open Graph tags** — Primary mechanism for Facebook, LinkedIn, WhatsApp, Telegram, Discord, Slack
2. **Twitter Cards** — `summary_large_image` type for X/Twitter
3. **JSON-LD (Schema.org)** — `Person` on homepage, `WebPage`/`SoftwareApplication` on project detail
4. **Per-page dynamic metadata** — Each page provides unique title, description, image, URL
5. **Fallback defaults** — Site-wide defaults via context processor
6. **Canonical URLs via SITE_URL** — Environment-configured base URL for absolute URLs
7. **OG images in staticfiles** — Served via WhiteNoise with versioned filenames for caching

## Alternatives Considered
- **Only Open Graph** — Insufficient for X/Twitter optimal display
- **Only Twitter Cards** — Doesn't cover Telegram/WhatsApp/LinkedIn/Facebook
- **Client-side rendering** — Crawlers don't execute JS; meta tags must be in initial HTML
- **External image CDN** — Unnecessary complexity; WhiteNoise + Runflare static hosting sufficient

## Consequences
### Positive
- Rich previews on all target platforms
- Better SEO via structured data
- Maintainable: single partial template, page-specific overrides
- Cache-friendly: staticfiles with WhiteNoise hashing

### Negative
- Migration required for `Project.og_image` field
- Must maintain `SITE_URL` in deployment environment
- OG images duplicated in `public/media/` (for Runflare) and `staticfiles/` (for WhiteNoise)

## Implementation Notes
- Reusable partial: `portfolio/templates/portfolio/partials/_meta_tags.html`
- Context processor: `portfolio.context_processors.site_meta`
- Template blocks per page: `og_title`, `og_description`, `og_image`, `og_type`, `og_url`
- JSON-LD block: `json_ld` in `base.html`
- Twitter card type: `summary_large_image` (1200×630)