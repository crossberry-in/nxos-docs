# GEMINI.md — nxos-docs instructions (Gemini CLI)

Read `AGENTS.md` first — it is the canonical rule set for this
documentation repository. The rules below restate it for Gemini.

## Facts you must never contradict

- Ubuntu 24.04 LTS ARM64 is the only installable Noxs environment; Kali is
  planned; Noxs ≠ NoxOS.
- SAF storage is command-based (never a POSIX mount); /sdcard is an opt-in.
- Verify every command against crossberry-in/noxs source before documenting.
- Example outputs are examples, not verified device output.

## Workflow

1. Inspect the existing page and mkdocs.yml nav before editing.
2. Preserve working routes; no duplicate pages.
3. `mkdocs build --strict` must pass before you commit.
4. Conventional commit; PRs validated by docs-validate.yml.
5. After merge, verify the deployed site before claiming success.
