---
name: documentation-audit
description: Full documentation audit
---

# nxos-docs skill: documentation-audit

purpose: Audit the whole site for drift, broken links, stale facts.
when_to_use: Periodic audits; before releases; after big app changes.
required_context: The deployed sitemap is the route baseline; noxs repo metadata is the fact baseline.
relevant_files:
  - docs/** (all)
  - mkdocs.yml
workflow:
  1. Fetch https://crossberry-in.github.io/nxos-docs/sitemap.xml — every old route must still resolve or be redirected by nav.
  2. Walk sections; verify commands against source; verify statuses.
  3. Produce a findings list (page, issue, fix) — fix in the same PR.
coding_rules: Report honestly; no "assume fixed".
security: Audit for leaked secrets too.
testing: mkdocs build --strict + link check.
documentation_updates: the task itself.
checklist:
  - route baseline intact
  - findings fixed
