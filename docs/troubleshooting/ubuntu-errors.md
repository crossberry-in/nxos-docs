# Ubuntu Errors

Errors inside the Ubuntu 24.04 environment, with the verified repair
path for each.

## `apt` says "Unable to locate package <name>"

Package lists are empty (bootstrap never completed). Run:

```console
noxs@ubuntu:~$ nx cert-fix
```

## `apt update` fails with certificate/TLS errors

Broken CA bundle or sources. Run `nx cert-fix` — it refreshes the CA
bundle, repairs `noxs.sources`, and verifies the result. Details:
[Certificate errors](certificate-errors.md).

## "Reading package lists... Error" / dpkg errors

Interrupted dpkg configuration:

```console
noxs@ubuntu:~$ sudo dpkg --configure -a
```

Startup repairs this automatically too ("Checking for interrupted dpkg
configuration"). For a corrupted dpkg status database, the app repairs
from `status-old` where possible; `nx pkg doctor` reports the state.

## Keyring warnings / NO_PUBKEY

The official keyring is installed as `ubuntu-keyring` with
`/usr/share/keyrings/ubuntu-archive-keyring.gpg`. If a repair removed
it, `nx cert-fix` reinstalls it. Check with:

```console
noxs@ubuntu:~$ noxs ubuntu status
```

## "Unable to acquire the dpkg frontend lock"

Another package operation is running (single-flight lock
`/run/noxs/pkg-tx`). Wait for it to finish; concurrent package
managers refuse to start rather than corrupt the database.

## Forgot the `noxs` password

Reset it from the app (terminal settings / user management screen).
The password is used by `sudo` inside the sandbox only and is never
stored by the app.

## `noxs ubuntu status` shows "package index: EMPTY"

Run `nx pkg update` (or `sudo apt update`) to populate the index. See
[Linux package management](../environments/linux-package-management.md).

## Session shows `✗ FAILED (code)`

The shell exited with an error — check the command's output; the
session status line shows the code. Restart the session from the
terminal's session tabs.
