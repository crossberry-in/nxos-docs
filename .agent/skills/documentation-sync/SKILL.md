---
name: documentation-sync
description: Docs sync pipeline (docs-repo side)
---

# nxos-docs skill: documentation-sync

purpose: Handle incoming docs-sync tasks and PRs from the noxs repo.
when_to_use: _sync/ review tasks appear; docs-sync PRs arrive.
required_context: The noxs repo's docs-sync workflow files review tasks under _sync/; it never overwrites content automatically.
relevant_files:
  - _sync/*.md (generated task lists)
  - .github/workflows/docs-validate.yml
workflow:
  1. Read the task: source commit + affected pages (mapped by doc_sync.py affected).
  2. Inspect the referenced app commit; update ONLY the affected pages.
  3. Strict build; PR review; merge deploys.
coding_rules: Never auto-merge; review every generated task.
security: Task files come from CI with least-privilege tokens only.
testing: strict build.
documentation_updates: the task itself.
checklist:
  - tasks processed and removed after completion
  - pages updated match the mapping
