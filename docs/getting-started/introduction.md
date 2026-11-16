# Introduction — What is Noxs?

Noxs is an Android terminal application that runs a **real Linux
userspace on your phone or tablet** — no root, no custom recovery, no
security bypass. Inside the Android application sandbox it downloads a
genuine distribution root filesystem and runs it through
[proot](https://proot-me.github.io/) with a real PTY terminal, a real
editor, a real package system and a permission-first Android
integration layer.

```console
noxs@ubuntu:~$ uname -a
Linux localhost 5.10.236-android12 … aarch64 Android host kernel via proot
noxs@ubuntu:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04.5 LTS"
```

*(Illustrative session output — the exact kernel string depends on your
device.)*

## What is Noxs?

| Layer | What you get |
|---|---|
| **Terminal** | A clean-room VT/xterm engine, native PTY (`forkpty`), scrollback, search, gestures, multiple sessions |
| **Linux environments** | [Ubuntu 24.04 LTS](../environments/ubuntu-installation.md) is the installable environment; [Kali Linux is planned](../environments/kali-installation.md); legacy Debian installs of upgrading users are imported read-only |
| **CLI** | The [`noxs` core CLI](../cli/noxs.md) and the [`nx` command system](../cli/nx.md) — packages, AI, plugins, storage, Android bridge |
| **Android integration** | SAF file access, Photo Picker, camera, notifications, clipboard, share, device reports — [all optional, all revocable](../android/overview.md) |
| **Developer tools** | `apt`-installable toolchains plus the built-in [code-server editor](../devtools/code-server.md) |
| **Package system** | The [NX Package System](../packages/package-manager.md): Git-based packages, `nx install`, `nx pkg`, NXMirror Cloud |
| **AI** | The [`nx ai` agent terminal](../ai/nx-ai.md) — tool-using agent loop with explicit approvals |
| **Extensibility** | [Plugin SDK](../plugins/plugin-sdk.md) and the [`@noxs/nx-api` SDK](../plugins/nx-api.md) behind the Permission Center |

## Available · Experimental · Planned · Unsupported

Noxs documents features honestly. This site labels every capability:

- **Available** — implemented, tested and shipped in the current release
  (v1.3.x). Everything in [Getting started](installation.md) and the
  [command reference](../reference/cli-reference.md) is in this category.
- **Experimental** — usable but with known limits, clearly stated in the
  page (for example the [Docker compatibility layer](../cli/docker.md)
  and the [opt-in `/sdcard` direct mount](../android/external-sdcard.md)).
- **Planned** — designed or modeled but **not shipped**. [Kali Linux
  environments](../environments/kali-installation.md) are in this
  category today. Planned features are never presented as working.
- **Unsupported** — out of scope by design: Android root, modifying the
  Android system, evading SELinux/Play Protect, bulk or silent SMS.

## Noxs and NoxOS are different products

**Noxs** (this documentation) is the Android terminal app by
CrossberryWeb. **NoxOS** is a separate emulator track; Noxs integrates
with it as a companion, documented in
[NoxOS Emulator](../architecture/noxos-emulator.md). Do not treat the
two names as one product.

## Where to go next

1. [Installation](installation.md) — get the APK from GitHub Releases.
2. [First launch](first-launch.md) and [Initial setup](initial-setup.md).
3. [Quick start](quick-start.md) — ten minutes to a productive terminal.
4. [System requirements](system-requirements.md) if you are unsure your
   device qualifies.
