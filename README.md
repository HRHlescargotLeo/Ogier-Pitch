# Ogier — website roadmap concepts

Concept designs prepared by ClerksWell for the Ogier pitch.

| File | Contents |
| --- | --- |
| `index.html` | Overview — what we found on the current site, and links to the four ideas |
| `idea-one.html` | Clearer routes into Ogier's expertise (two concepts) |
| `idea-two.html` | A digital concierge |
| `idea-three.html` | News and insights that answer the question |
| `idea-four.html` | An enquiry route that qualifies as it goes |

## Publishing to GitHub Pages

All five pages are self-contained (CSS and JS inline, no images, no build step) and link
to each other with relative paths, so they work from any folder.

1. Push the five `.html` files to a repository.
2. **Settings → Pages →** deploy from a branch, root folder.
3. The pack opens at the repository's Pages URL; the top navigation links between pages.

They also work by opening `index.html` directly from disk.

## Presenting

- Every concept is interactive — hovers, selections and second screens all function.
- Commentary is **hidden by default** so the interfaces read cleanly. *Show notes*, top
  right, brings back the rationale, effort estimates and suggested phasing.
- Designed for a 1280px-plus viewport; the pages reflow down to mobile.

## Sources and caveats

Palette (`#E40046` crimson, `#1C1F2A` ink), typography, service names, sector names,
jurisdictions, statistics and article titles are taken from ogier.com. The brand face is
Brown Std; Figtree is loaded as the closest freely available stand-in. Individual names
and job titles in the demos are placeholders. Nothing in the pack is legal advice.

## Rebuilding

`parts/` holds the page sources, `parts/css/` the per-concept stylesheets and
`parts/_shared.css` the design system. `python3 build.py` regenerates the five HTML files.
