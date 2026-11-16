# Installation

Noxs is distributed as a signed APK from the project's GitHub Releases.
There is no Play Store listing and no third-party mirror — always install
from `github.com/crossberry-in/noxs`.

## Where to download

Open <https://github.com/crossberry-in/noxs/releases> and take the
**latest** release. A v1.3.x release ships:

| Asset | What it is |
|---|---|
| `noxs-<version>-full.apk` | The full application (contains the bootstrap toolchain) — **recommended** |
| `noxs-<version>-lite.apk` | A small launcher APK; large components download during setup |
| installer / rootfs archives | Offline bootstrap assets used by the installer pipeline |
| `SHA256SUMS` | Checksums for every asset |

!!! tip "Which APK?"
    Use **full** when you want the smoothest first launch, **lite** when
    download size matters more than setup time. Both produce the same
    Ubuntu environment.

## Install steps

1. Download `noxs-<version>-full.apk` on an ARM64 Android device.
2. Verify the SHA-256 against `SHA256SUMS` if you can.
3. Open the APK and confirm the install prompt.
4. Continue with [First launch](first-launch.md).

## About Play Protect

Google Play Protect may show an unknown-source warning for any app
installed outside the Play Store. Noxs v1.3.1+ deliberately requests
**no sensitive permissions** for messaging: SMS sending hands the message
to *your own* SMS app, and the app holds no `SEND_SMS` permission at all.
If Play Protect still interposes a warning, verify that your APK really
came from the official Releases page before continuing.

## Supported devices

- **Architecture**: ARM64 (`arm64-v8a`) is the tested primary target;
  the installer also handles `armeabi-v7a` and `x86_64` builds, but the
  pinned Ubuntu rootfs on-device flow is ARM64-first. See
  [System requirements](system-requirements.md).
- **Android version**: Android 7.0 (API 24) or newer; Android 13+
  enables the modern media/Photo Picker paths.

## Updating

Install the new APK over the old one — your Linux environment, packages
and files are preserved (they live in app-private storage, untouched by
an app update). Downgrading is not supported and may require a
reinstall; see [Rootfs management](../environments/rootfs-management.md)
for what is kept where.
