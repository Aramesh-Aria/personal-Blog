# Context — Personal Portfolio (Aria Aramesh)

## Glossary

**Project**
: A portfolio item representing a software project. Has title, category, thumbnail image, optional custom Open Graph image (`og_image`), media (image/video/placeholder), overview sections, and features.

**OG Image (Open Graph Image)**
: A 1200×630 pixel image used for social link previews on platforms implementing the Open Graph protocol (Telegram, WhatsApp, Discord, Facebook, LinkedIn, etc.). Also used by Twitter/X Cards when `twitter:image` is not specified.

**SITE_URL**
: The canonical base URL of the deployed site (e.g., `https://aria-aramesh.ir`). Configured via environment variable. Used to construct absolute URLs for `og:url`, `og:image`, `twitter:image`, and JSON-LD `@id` fields.

**JSON-LD (Structured Data)**
: Schema.org markup embedded in `<script type="application/ld+json">` tags. Provides machine-readable metadata for search engines and social platforms. This project uses `Person` (homepage) and `WebPage`/`SoftwareApplication` (project detail).

**Twitter Card**
: Metadata format for X (Twitter) link previews. Uses `summary_large_image` type (1200×630 image). Falls back to Open Graph tags when Twitter-specific tags are absent.

**Fallback OG Image**
: The default `og-image.webp` used when a page has no specific preview image. Stored in staticfiles for CDN caching.

**Profile OG Image**
: The homepage preview image (`profile-4.webp`), a square portrait used for the `Person` schema and homepage Open Graph tags.

**WhiteNoise**
: Django middleware for serving static files in production with compression and cache-friendly hashed filenames. Used by this project.

**Runflare**
: The deployment platform. Serves static files from `public/static/` and media from `public/media/`. Requires OG images to exist in both locations.