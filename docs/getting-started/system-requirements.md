# System Requirements

The compatibility engine checks these requirements before an install
starts and refuses honestly when something is missing.

## Hardware and OS

| Requirement | Value | Notes |
|---|---|---|
| Android version | **7.0 (API 24) or newer** | `minSdk 24`; Android 13+ enables Photo Picker / media-permission paths |
| Architecture | **ARM64 (`arm64-v8a`) recommended** | ARM64 is the tested primary target; `armeabi-v7a` and `x86_64` are detected but the on-device Ubuntu flow is ARM64-first |
| RAM | **512 MB free minimum** | The compatibility check requires available RAM ≥ 512 MiB; more is strongly recommended for code-server, Docker and AI use |
| Storage | see below | Measured *inside* app-private storage, not the whole device |

## Storage

The pinned Ubuntu 24.04 (Noble) rootfs variant is sized:

| Phase | Estimate |
|---|---|
| Download | ≈ 30 MB |
| Extracted rootfs | ≈ 101 MB reserved (≈ 96 MB measured) |

The real requirement is larger than the sum of both, because the
download and the extraction reserves must co-exist during setup.
Practical guidance:

- **Fresh install**: keep ~1 GB free in internal storage.
- **With code-server**: add ~100–200 MB for the code-server install.
- **With Docker**: several hundred MB for images and layers — see
  [Docker support](../cli/docker.md).
- **Package work**: packages install into the environment root and
  grow it; `nx pkg doctor` reports free space.

## Network

- Required **once** for the initial download and the APT bootstrap.
- Required for package installs, code-server download, AI gateways and
  the plugin store.
- Not required for normal terminal use after bootstrap — everything in
  the environment works offline.

## Permissions

Nothing is required at install time. Storage, notifications, camera and
the opt-in direct mount are requested only when you use the matching
feature — see [Android app permissions](../android/app-permissions.md).

## Not supported

- Android emulators without `/proc` passthrough and ptrace support may
  fail — Noxs targets real ARM64 devices.
- Devices with Play Integrity-enforced enterprise policies that block
  sideloaded apps.
- Android Go devices with less than 512 MB available RAM (the check
  will refuse the install).
