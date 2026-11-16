# Package Errors

The stable error-code table with fixes lives in
[Package troubleshooting](../packages/package-troubleshooting.md).
This page covers the environment-side symptoms around package work.

## "Unable to locate package"

Empty package lists — run the repair:

```console
noxs@ubuntu:~$ nx cert-fix
noxs@ubuntu:~$ nx pkg update
```

## "Unable to acquire the dpkg frontend lock"

A package operation is already running (single-flight lock). Wait for
the other operation; check for stray apt/dpkg processes with
`noxs-ps`.

## `E: …` errors from apt

Common apt errors and their Noxs-specific context:

| Error | Cause | Repair |
|---|---|---|
| `E: Unable to locate package` | Empty lists | `nx cert-fix` then `apt update` |
| `E: Failed to fetch … 404` | Stale index or removed package | `sudo apt update` |
| `E: The repository … is not signed` | Broken keyring/sources | `nx cert-fix` (self-heals `noxs.sources`) |
| `dpkg was interrupted` | Interrupted configuration | `sudo dpkg --configure -a` |

## `nx install` fails with CHECKSUM_MISMATCH

The artifact on the release server does not match its published
digest — it was **not** installed. Report the broken release to the
package author; see the [error table](../packages/package-troubleshooting.md#stable-error-codes).

## `INSUFFICIENT_DISK_SPACE`

Check space in the guest (`df -h /`) and on Android; packages install
into the environment root — see
[System requirements](../getting-started/system-requirements.md#storage).

## `nx pkg doctor` warnings

`nx pkg doctor` validates identity, repos, keyring, dpkg state,
certificates, tools and storage; each `WARN` row prints its repair
hint. Run it after any failed install to confirm the layer is healthy
again.
