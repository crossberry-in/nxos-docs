# First Launch

After [installing](installation.md) Noxs, the first launch walks you
through environment setup with a fully automatic pipeline — you never
type installation shell commands.

## What you see

1. **Welcome screen** — the Noxs welcome activity states what the app
   is and what it will download.
2. **Install info** — Ubuntu 24.04 LTS branding, the storage
   requirement for your device, and the architecture check.
3. **Password prompt** — Noxs asks you to set the `noxs` user password.
   It is used by `sudo` *inside* the Linux environment and is never
   stored or transmitted. If you forget it, it can be reset from the
   app; see [Troubleshooting](../troubleshooting/ubuntu-errors.md).
4. **Download + verification** — the official Ubuntu rootfs is
   downloaded in stages and verified against a pinned SHA-256 before
   extraction starts.
5. **Safe extraction + configuration** — TarGuard extraction, DNS,
   locale, the `noxs` user, official APT sources.
6. **Terminal opens** at the prompt:

```console
noxs@ubuntu:~$
```

The whole flow is tracked with honest progress: spinner + elapsed time
per operation, real byte counts for downloads, real entry counts for
extraction — no fake percentages. Long operations print a single
"Still working…" notice; long is not an error.

## What first launch does NOT do

- It does not request storage, SMS or contacts permissions.
- It does not modify any Android system path.
- It does not start background services you did not ask for.

## After the first launch

Head to [Quick start](quick-start.md) for the first commands worth
running, or [Initial setup](initial-setup.md) for the full setup
walkthrough and what each stage installs.
