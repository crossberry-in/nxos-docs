---
name: cli-reference
description: CLI reference accuracy
---

# nxos-docs skill: cli-reference

purpose: Keep docs/reference/cli-reference.md and per-command pages in sync with the real CLI.
when_to_use: Any CLI change in the noxs app repo; help text changes.
required_context: The canonical sources are NoxsCliTemplate.kt and NoxsNxTemplate.kt; the app-side metadata registry is app/src/main/resources/documentation/commands.json.
relevant_files:
  - docs/reference/cli-reference.md
  - docs/cli/*.md
workflow:
  1. Diff the CLI template against the current reference table (new commands? removed?).
  2. Update options/examples; every command row needs a verified purpose.
  3. Cross-check `noxs docs` topic list against NoxsDocsMap.kt.
coding_rules: Only real commands; unknown/unsupported flags never documented.
security: Examples never contain real numbers, keys or private data.
testing: doc_sync.py check (app repo) + strict build here.
documentation_updates: the task itself.
checklist:
  - reference table matches dispatch
  - docs topics match NoxsDocsMap
