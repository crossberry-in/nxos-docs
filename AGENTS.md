# nxos-docs — Agent Instructions (canonical)

Read this file before editing anything in this documentation repository.
Tool-specific files (GEMINI.md, CLAUDE.md, .github/copilot-instructions.md)
repeat these rules for their agents; if they disagree, this file wins.

## What this site documents

Noxs by CrossberryWeb — an Android terminal app providing a genuine
Ubuntu 24.04 LTS ARM64 userspace through proot
(source: [crossberry-in/noxs](https://github.com/crossberry-in/noxs),
site: https://crossberry-in.github.io/nxos-docs/).

**Fact baseline (never contradict it):**

- Ubuntu 24.04 LTS ARM64 is the ONLY installable environment. There is no
  distribution selector and no Debian fallback.
- Kali Linux ARM64 is PLANNED. Kali pages stay marked planned until the
  app actually ships a Kali provider.
- Noxs is NOT the private NoxOS project — never describe NoxOS internals,
  its emulator, or private source as Noxs features.
- SAF storage is command-based and never a POSIX mount; the /sdcard bind is
  an explicit two-step opt-in.
- Noxs holds no SMS permission; sending goes through the system SMS app.
- proot gives app-sandbox isolation — never claim hardware-virtualization or
  separate-device security.

## Repository layout

- `docs/` — Markdown pages (Material for MkDocs), organized by section:
  getting-started/, environments/, terminal/, cli/, android/, files/,
  devtools/, packages/, plugins/, ai/, architecture/, troubleshooting/,
  reference/, changelog.md.
- `mkdocs.yml` — nav + theme. Every page must be reachable from nav.
- `assets/style.css` — Apple-inspired styling (system font stack).
- `.github/workflows/deploy-pages.yml` — Pages deployment (push to main).
- `.github/workflows/docs-validate.yml` — PR validation (strict build).
- `_sync/` — auto-generated review tasks from the noxs docs-sync workflow.

## Non-negotiable rules

1. Inspect existing pages before editing; preserve working routes. A route
   that ever appeared in the deployed sitemap must not become a 404.
2. Verify every CLI command against the real implementation in
   crossberry-in/noxs (`NoxsCliTemplate.kt`, `NoxsNxTemplate.kt`) before
   documenting it. Never invent commands, options, or outputs.
3. Example outputs are examples — never claim they are verified device
   output unless captured from a real session.
4. Prompts in examples use `noxs@ubuntu:~$`.
5. Keep Ubuntu and Kali documentation separate and truthful.
6. Never publish API keys, tokens, credentials, or private source.
7. Every internal link must resolve (`mkdocs build --strict` fails on
   broken links — keep it that way).
8. One topic per page; avoid duplicate pages for the same command.

## Workflow for every change

1. Read the page + its neighbors; check `mkdocs.yml` nav.
2. Make the edit; keep terminology consistent (SAF, rootfs, userspace).
3. `pip install -r requirements.txt && mkdocs build --strict` locally.
4. If the change mirrors an app change, reference the source commit.
5. Conventional commit message (`docs(storage): ...`).
6. PRs are validated by docs-validate.yml; deployment happens on merge to
   main — verify https://crossberry-in.github.io/nxos-docs/ after merge
   before reporting success.

## Definition of done

- [ ] `mkdocs build --strict` passes.
- [ ] All internal links resolve; no orphan pages (nav updated).
- [ ] Commands verified against the app source.
- [ ] Statuses accurate (implemented / experimental / planned).
- [ ] No invented facts, no leaked secrets, no broken routes.
