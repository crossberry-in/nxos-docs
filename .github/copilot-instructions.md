# GitHub Copilot instructions — nxos-docs

`AGENTS.md` is the canonical rule set; these instructions restate it.

- Noxs docs (Material for MkDocs). Ubuntu 24.04 LTS ARM64 is the only
  installable environment; Kali is planned; Noxs ≠ NoxOS.
- Verify commands against crossberry-in/noxs source; never invent APIs,
  options, or outputs. Example outputs are examples only.
- Preserve existing routes and nav entries; one topic per page.
- `mkdocs build --strict` must pass before committing.
- Conventional commit messages; never leak secrets or private source.
