---
name: release-notes
description: Changelog and release notes
---

# nxos-docs skill: release-notes

purpose: Write truthful changelog entries for nxos-docs changelog.md.
when_to_use: App releases or notable documentation changes.
required_context: Implemented → tested → merged → released are distinct stages; never claim released without a tag.
relevant_files:
  - docs/changelog.md
workflow:
  1. Group entries: Added / Changed / Fixed / Removed / Security / Breaking.
  2. Reference the real app version/tag; no invented versions.
  3. Documentation-only changes get their own entries when user-visible.
coding_rules: Concise, factual, user-focused ("what changes for you").
security: No credentials in examples.
testing: strict build.
documentation_updates: the task itself.
checklist:
  - entries match real releases
  - stage wording accurate
