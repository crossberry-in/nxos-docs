# nxos-docs

Full documentation site for **Noxs** — a real **Ubuntu 24.04 LTS**
Linux environment for Android (with a planned Kali track; legacy
Debian installs of upgrading users are imported read-only).

- **70+ pages** organized into Getting Started, Linux Environments,
  Terminal, NX Command System, Android Integration, File Manager,
  Developer Tools, Package Manager, AI Integration, Plugin SDK,
  Architecture & Security, Troubleshooting, API Reference and
  Changelog.
- Built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
  and deployed to **https://crossberry-in.github.io/nxos-docs/** by
  `.github/workflows/deploy-pages.yml` on every push to `main`.
- Content is written against the actual Noxs source code
  ([crossberry-in/noxs](https://github.com/crossberry-in/noxs)); every
  command, permission and capability documented here is verified.
  Features are labeled **available / experimental / planned /
  unsupported** — planned features (e.g. Kali) are never presented as
  working.
- Apple-inspired design layer (`docs/assets/style.css`): glass
  surfaces, rounded panels, system font stack, dark/light themes,
  responsive layout.

## Rebuilding locally

```bash
pip install "mkdocs-material==9.7.7"
mkdocs build --strict   # output in site/
mkdocs serve            # live preview at http://127.0.0.1:8000
```

QA helpers:

```bash
python3 scripts/check_links.py   # verify every relative link + anchor
```

## Documentation audit (2026-11)

- Restructured the nav into the section set the site ships today and
  moved all pages into matching directories (old flat filenames
  redirect via the new nav; internal links rewritten and
  link-checked).
- Rewrote the home page and all Getting Started pages
  (introduction, installation, first launch, initial setup, system
  requirements, quick start, FAQ) — Ubuntu-first, Debian demoted to a
  legacy-import note.
- Added the Kali Linux pages with an explicit **planned** status
  (the source ships Ubuntu only — nothing invented).
- Added File Manager, Developer Tools, AI Integration (config,
  providers, API keys), Plugin manifest/lifecycle, Troubleshooting,
  API Reference (CLI/configuration/manifests/SDK/errors) and a
  Changelog.
- Updated outdated pages (bootstrap system, cert-fix, mirror,
  architecture diagram labels, permission catalog with the
  v1.3.1 no-SMS-permission flow).
