---
name: documentation-writing
description: Writing accurate Noxs documentation pages
---

# nxos-docs skill: documentation-writing

purpose: Create or update docs pages with verified, honest content.
when_to_use: Any new or edited page under docs/.
required_context: AGENTS.md fact baseline; the app source for command truth.
relevant_files:
  - docs/** (sections: getting-started, environments, terminal, cli, android,
    files, devtools, packages, plugins, ai, architecture, troubleshooting, reference)
  - mkdocs.yml (nav)
workflow:
  1. Read the target page + neighbors; find the natural place for the change.
  2. Verify commands against NoxsCliTemplate.kt / NoxsNxTemplate.kt in the noxs repo.
  3. Write with `noxs@ubuntu:~$` prompts; mark example output as example.
  4. Add the page to mkdocs.yml nav (or extend an existing page to avoid duplicates).
coding_rules: Present tense, plain English, one topic per page, first-use term explanations.
security: Never include credentials or private NoxOS information.
testing: mkdocs build --strict.
documentation_updates: the task itself.
checklist:
  - commands verified against source
  - nav updated
  - strict build passes
