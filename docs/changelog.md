# Changelog — Release History

Release artifacts, notes and downloads live at
<https://github.com/crossberry-in/noxs/releases>. This page summarizes
the release line; entries below only state verified facts.

## Release line

| Version | Status |
|---|---|
| **v1.3.1** | current |
| v1.3.0 | superseded |
| v1.0.0 – v1.2.1 | archived |
| v0.1.0 – v0.16.1 | development line |

## v1.3.1 — Play-Protect-friendly messaging (current)

- **All SMS now goes through your own SMS app.** `noxs sms send` /
  `compose` open the system messaging app with the message prefilled;
  you press send there. Noxs requests **no SMS permission at all**
  (`SEND_SMS` fully removed) — resolving Google Play Protect's
  sensitive-permission block on install.
- Permission Center, CLI usage text and docs updated to the
  permission-free SMS flow.
- Device/network reports hardened (non-identifying summaries only).

## v1.3.0 — Ubuntu-first environment + release pipeline hardening

- Ubuntu-first environment line: fresh installs run the pinned,
  official **Ubuntu 24.04 LTS (Noble)** rootfs from `cdimage.ubuntu.com`
  with SHA-256 pinning and TarGuard safe extraction.
- Legacy Debian installs of upgrading users are imported read-only —
  never erased, never reinstalled.
- CI release pipeline fixes: manifest/XML, shellcheck findings, docs
  navigation, editor filesystem compile issue and status-report
  unit-test alignment.

## Milestones (verified anchors from earlier releases)

| Version | Milestone |
|---|---|
| v0.11.0 | Noxs Plugin SDK **0.0.1** (logging, ui, terminal) shipped host-side |
| v0.13.0 | Plugin-scoped **storage** feature (SDK **0.0.2**) |
| v1.0.0 | First stable release line |

Full notes for every archived release are on the
[GitHub Releases page](https://github.com/crossberry-in/noxs/releases) —
this page intentionally does not paraphrase those entries.

## Deprecations and breaking changes

- **Debian-first installs** — replaced by the Ubuntu-first flow
  (v1.3.0). Existing Debian environments continue as read-only legacy
  imports; no silent removal, ever.
- **`SEND_SMS` usage** — removed in v1.3.1. Automations that expected
  silent sending must move to the compose flow (the user always
  presses send).

## NoxOS and other products

NoxOS emulator releases are a separate track — see
[NoxOS Emulator](architecture/noxos-emulator.md). This changelog covers
the Noxs Android app only.
