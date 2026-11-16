# Kali Linux Installation — Planned

!!! warning "Status: planned — not available in the current release"
    Noxs ships exactly **one** installable environment: **Ubuntu 24.04
    LTS**. There is no Kali download path, no distribution selector and
    no Kali provider in the current app. This page describes the
    **planned** Kali track; nothing below is installed or guaranteed
    until it ships.

## Where Kali support stands today

- The environment data model already defines Kali installable variants
  (`Kali full / minimal / nano`, including a *NetHunter Rootless* flavor)
  and the multi-environment registry, switching and storage layout are
  built to hold more than one environment.
- The provider registry currently registers **only** `UbuntuProvider`.
  No Kali rootfs pipeline, no Kali bootstrap manifest and no Kali
  release asset exist yet.
- The Android-integration storage flows (SAF categories, direct mount)
  are environment-agnostic and will work in any future environment.

## What the planned track will look like

Design goals, subject to change before release:

1. **Download source** — official Kali rootfs artifacts only, pinned
   SHA-256, staged download and TarGuard extraction, exactly like the
   Ubuntu pipeline.
2. **Identity** — `noxs@kali:~$` prompt, `noxs` user, Kali apt sources
   over HTTPS.
3. **Switching** — installed environments appear in the environment
   manager; switching does not reinstall and does not touch other
   environments' files.
4. **Same CLI** — `nx`/`noxs` commands, the package system and the
   Android bridge are environment-independent.

## What you can do today

- Run **Ubuntu 24.04 LTS** — see
  [Ubuntu installation](ubuntu-installation.md).
- Use **Kali-flavored tooling inside Ubuntu** by installing packages
  from Ubuntu's repositories (many Kali tools are Debian packages, but
  Kali's own repositories are **not** supported in Noxs today).
- Upgrading users with a legacy Debian environment keep it as a
  read-only import — see
  [Environment switching](environment-switching.md).

## Watch this page

When the Kali provider ships, this page will document the real
download, verification and first-launch flow — with verified facts only.
Do not attempt to hand-install foreign rootfs tarballs into the app's
private storage; that path is not supported and will be replaced by the
official installer flow.
