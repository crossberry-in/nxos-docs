# Installation Errors

Setup is honest about failures: every stage keeps its real error text
and the operation record shows `✗ <name> <elapsed>`. Match your
symptom below.

## Storage check fails ("not enough space")

- The installer reserves download **and** extraction space
  (≈ 30 MB download / ≈ 101 MB extracted, plus working room).
- Free space (Android Settings → Storage) and retry; ~1 GB free is a
  comfortable target — see
  [System requirements](../getting-started/system-requirements.md).

## "Integrity verify" aborts

- The rootfs SHA-256 is pinned; a mismatch aborts the install by
  design (corrupt or tampered download).
- Retry on a stable network. Repeated failures: check that no
  "private DNS"/VPN is rewriting downloads, then reinstall the app
  from the official release.

## Extraction fails

- TarGuard rejects malformed archives; a failed extraction never
  leaves a half-installed rootfs in the active path.
- Retry the setup. If it persists across networks, report it with the
  setup log (the console keeps the full transcript).

## Setup stuck at "APT bootstrap"

- The bootstrap is **non-fatal by design**: a failed first update
  schedules background repair and the environment still opens.
- Inside the terminal, run [`nx cert-fix`](../cli/cert-fix.md) to
  complete the certificate + sources repair manually — see
  [Certificate errors](certificate-errors.md).

## Setup interrupted (app closed, reboot)

- The task manager scans for interrupted setups on next start
  (`scanForRecovery`) and offers recovery instead of restarting from
  zero.
- Interrupted dpkg configuration is detected and repaired at startup.

## Architecture not supported

- The installer checks the device architecture; the on-device Ubuntu
  flow is ARM64-first. See
  [System requirements](../getting-started/system-requirements.md).

## Still failing?

- `noxs status` / `noxs ubuntu status` in the terminal show what is
  broken and the matching repair hint.
- Report at <https://github.com/crossberry-in/noxs/issues> with the
  setup console output (it is copy-paste friendly).
