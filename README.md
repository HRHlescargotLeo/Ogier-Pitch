# Ogier — website roadmap concepts

Concept designs prepared by ClerksWell for the Ogier pitch.

| File | Contents |
| --- | --- |
| `index.html` | Overview: what we found on the current site, and links to both idea sets |
| `idea-one.html` | Idea One — three concepts for the homepage audience-routing component |
| `idea-two.html` | Idea Two — three concepts for an AI-powered digital concierge |

## Publishing to GitHub Pages

The three pages are fully self-contained (all CSS and JS inline, no images, no build
step) and link to each other with relative paths, so they work from any folder.

1. Push `index.html`, `idea-one.html` and `idea-two.html` to a repository.
2. **Settings → Pages →** deploy from a branch, root folder.
3. The pack opens at the repository's Pages URL; the top navigation links between pages.

They also work by opening `index.html` directly from disk.

## Presenting

- Every concept is interactive — hovers, clicks and second screens all work.
- **Hide notes** (top right) strips the commentary and leaves only the interface,
  for clean screenshots or a live walkthrough.
- Designed for a 1280px-plus viewport; the pages reflow down to mobile.

## Sources and caveats

Palette (`#E40046` crimson, `#1C1F2A` ink), typography, service names, sector names,
jurisdictions, statistics and article titles are taken from ogier.com. The brand face
is Brown Std; Figtree is loaded as the closest freely available stand-in. Individual
names and job titles in the demos are placeholders. Nothing in the pack is legal advice.

## Rebuilding

`parts/` holds the shared stylesheet and per-page sources; `python3 build.py`
regenerates the three HTML files.
