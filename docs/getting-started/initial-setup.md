# Initial Setup

This page explains what the initial setup pipeline actually does, stage
by stage. You watch it in the setup console; there are no commands to
type. The deep technical version lives in
[Ubuntu installation](../environments/ubuntu-installation.md).

## Setup stages

| # | Stage | What happens |
|---|-------|--------------|
| 1 | Welcome | Welcome activity, environment branding |
| 2 | Install info | Storage requirements, ARM64 check |
| 3 | Architecture detect | `arm64-v8a` (also `armeabi-v7a` / `x86_64` detection) |
| 4 | Storage check | Download + extraction reserves are verified |
| 5 | Rootfs acquisition | Official `ubuntu-base-24.04.5-base-arm64.tar.gz` from `cdimage.ubuntu.com`, staged download |
| 6 | Integrity verify | Pinned SHA-256 must match, else the install aborts |
| 7 | Safe extraction | TarGuard extraction into app-private storage |
| 8 | Userspace config | DNS, hosts, hostname, locale `C.UTF-8`, `noxs` user, `noxs@ubuntu` prompt, official APT sources |
| 9 | noxs user + password | `/home/noxs`, password collected in the console (never stored) |
| 10 | Runtime state | `/run`, `/var/run/noxs`, logs, resource quotas |
| 11 | APT bootstrap | Signed HTTP update → `ca-certificates` + `ubuntu-keyring` → verified HTTPS update |
| 12 | Terminal | Ubuntu launches through proot → `noxs@ubuntu:~$` |

## The `noxs` user and sudo

Setup creates a regular Linux user `noxs` with home `/home/noxs` and
adds it to the `sudo` group. `sudo` inside Noxs manages **only the
sandbox environment** — it is not Android device root, and proot's
fake-root (`proot -0`) is not Android root either. The welcome screen,
terminal banner and Security screen all state this.

## What lives where on Android

Everything is stored inside the app's private storage
(`/data/data/com.crossberry.noxs/…`):

```
files/noxs/                 base
  rootfs/                   the Ubuntu filesystem (guest /)
    home/noxs/              your home — exposed to the system Files app
                             as "Noxs Linux Home"
  run/                      control dirs bound to /var/run/noxs in the guest
```

No path outside the app sandbox is ever written.

## Legacy Debian installations

Upgrading users with an existing Debian 12 environment are **not**
force-migrated: the legacy environment is imported read-only as
"Debian 12 (legacy)" and keeps working. A `tar.gz` backup of your old
home can be produced and restored into the Ubuntu environment — see
[Backup and restore](../environments/backup-restore.md).

## Verifying the setup

```console
noxs@ubuntu:~$ noxs ubuntu status
Ubuntu environment status
  pretty name:  Ubuntu 24.04.5 LTS
  ...
```

If any stage failed, see
[Troubleshooting → Installation errors](../troubleshooting/installation-errors.md).
