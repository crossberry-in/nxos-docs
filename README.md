# nxos-docs

Public documentation site for **NoxOS** - an independent no_std Rust kernel for AArch64, verified only inside a QEMU sandbox.

- Content and screenshots are generated from the main repository [crossberry-in/NoxOS](https://github.com/crossberry-in/NoxOS) (see `scripts/build_docs_site.py` there).
- Deployed to GitHub Pages via the included workflow `.github/workflows/deploy-pages.yml` on every push to `main`.
- All screenshots are genuine QMP screendumps of the running kernel (720x1280 virtio-gpu). Nothing is mocked.

## Rebuilding the site

From the NoxOS repository: `python3 scripts/build_docs_site.py`
