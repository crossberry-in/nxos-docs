# Environment Switching

Noxs supports multiple Linux environments through the environment
manager. Today it ships one installable environment (Ubuntu 24.04 LTS);
legacy Debian installs of upgrading users appear as a second,
read-only-imported environment — and the same machinery will carry the
planned [Kali track](kali-installation.md).

## The registry

Environments are recorded in an app-private registry
(`environments/registry.json`) with id, provider, display name, status
and storage path. A separate `active.txt` records which environment new
terminal sessions launch against.

- Fresh installs get **Ubuntu 24.04 LTS (Noble Numbat)** only.
- Existing (pre-migration) Debian installs are imported as
  **Debian 12 (legacy)** — never erased, never reinstalled.

## Switching the active environment

Switching happens in the app's environment manager screen and
**never reinstalls**: it changes the registry's active id and restarts
the runtime service so new sessions spawn against the new paths. The
system Files entry ("Noxs Linux Home") follows the active environment —
the documents provider serves the *active* rootfs's `/home/noxs`.

Consequences worth knowing:

| Area | Behavior on switch |
|---|---|
| Terminal sessions | New sessions use the new environment; already-running sessions keep their old rootfs until closed |
| Files app root | Follows the active environment |
| Installed packages | Belong to each environment's own rootfs |
| Storage grants (SAF + direct mount) | Shared across environments — they are app-level, not per-rootfs |

## Legacy Debian import (migration source)

On an upgrading install, Noxs detects the legacy Debian base via its
install marker and imports it read-only as the active environment so
nothing breaks:

1. `classifyInstall` reads `.noxs-installed-v1` — `suite=bookworm` (or
   no `distro=` key) → legacy Debian; `distro=ubuntu` / `suite=noble` →
   Ubuntu.
2. The legacy environment is registered with status READY and used
   until you explicitly install Ubuntu.
3. Installing Ubuntu is an explicit user action through the setup flow.
4. A `debian-home-backup-<utc>.tar.gz` archive can be produced and
   restored into the Ubuntu home — see
   [Backup and restore](backup-restore.md).

## Removing an environment

Removal is explicit and user-confirmed only. It deletes that
environment's storage path, invalidates cached size figures and clears
the record — other environments and their data are untouched. Removal
never runs while a setup task is active for that environment.
