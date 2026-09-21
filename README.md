# hyperbounce-site

Marketing site for **Hyper Bounce**, an original neon brick-breaker by VibeDeV,
published by VIBECORE DIGITAL.

Served at <https://vibedev1229.github.io/hyperbounce-site/> and used as the
**Marketing URL** on the App Store product page, where it renders as
"Developer Website".

## Assets

Everything on the page is the real thing, not a mockup:

- `assets/icon.png` - the actual 1024 App Store icon shipped in the build
- `assets/shot-*.png` - the actual 1242x2688 App Store screenshots
- `assets/badge-appstore.svg` - Apple's official badge (Apple Marketing Tools)
- `assets/badge-googleplay.png` - Google's official badge
- `assets/hero.png` - the only generated art: an abstract backdrop (FAL flux/schnell),
  deliberately containing no objects, characters or text, so it cannot read as a
  second, different-looking version of the game
- `assets/og-image.png` - composed locally from the backdrop + the real icon +
  the game's own fonts (Orbitron, Rajdhani)

## Badge sizing

Apple's SVG is the bare badge. Google's PNG has its required clear space baked in,
so it is set taller (80px vs 54px) to make the two read as the same visual height.

## On App Store approval

The App Store badge is intentionally **unlinked** and marked "Coming soon", because
`https://apps.apple.com/app/id6812983236` 404s until the app is live. Swap the
`<span class="badge-soon">` block for a normal `<a class="badge-appstore" href="...">`
once it is approved. The comment in `index.html` marks the exact spot.
