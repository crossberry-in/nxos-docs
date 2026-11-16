---
name: mkdocs-maintenance
description: MkDocs configuration and build health
---

# nxos-docs skill: mkdocs-maintenance

purpose: Keep mkdocs.yml, theme, assets and the build green.
when_to_use: Nav changes, theme tweaks, build failures, dependency updates.
required_context: Material for MkDocs; requirements.txt pins the build deps; Pages deploys from main.
relevant_files:
  - mkdocs.yml
  - requirements.txt
  - assets/style.css
  - .github/workflows/deploy-pages.yml
workflow:
  1. Never drop a nav entry that resolves to an existing page (orphan pages break coverage).
  2. Run mkdocs build --strict locally; fix every warning.
  3. Keep the Apple-inspired styling conventions (system font stack, minimal chrome).
coding_rules: No framework migrations (Material stays); no heavy client JS.
security: Keep usesCleartext-equivalent hygiene — https links only in content.
testing: mkdocs build --strict + local preview (mkdocs serve).
documentation_updates: README when build steps change.
checklist:
  - strict build green
  - nav complete
