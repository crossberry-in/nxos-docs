# nxos-docs

Full documentation site for **Noxs** — a Debian-optimized Linux environment
for Android (and its NoxOS emulator track).

- 30+ feature pages: Ubuntu setup, terminal UX, NX package system, AI agent,
  Android integration, Permission Center, security model, plugins, App
  Center, NoxOS emulator, testing and more.
- Built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
  and deployed to **https://crossberry-in.github.io/nxos-docs/** by
  `.github/workflows/deploy-pages.yml` on every push to `main`.
- Content is mirrored from the main repository
  [crossberry-in/noxs](https://github.com/crossberry-in/noxs) (`docs/` +
  `mkdocs.yml`, single source of truth).
- The superseded hand-written HTML pages were removed; the classic QEMU
  screenshots remain under `screenshots/`.

## Rebuilding locally

```bash
pip install "mkdocs-material==9.7.7"
mkdocs build --strict   # output in site/
mkdocs serve            # live preview at http://127.0.0.1:8000
```
