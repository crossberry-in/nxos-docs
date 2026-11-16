# Package Installation — `nx install`

`nx install` is the user-facing installer of the NX Package System. It
resolves a package, verifies it end-to-end and extracts it into the
environment — with a live single-line progress UI.

## Syntax

```console
noxs@ubuntu:~$ nx install <name>[@version]        # official noxs-pkg package
noxs@ubuntu:~$ nx install -git @user/repo[@version]  # any GitHub repo with registry.json
```

Aliases: `nx pkg install <name>` starts the same flow through the
distro-aware front end (which additionally handles apt packages).

## The install flow

1. **Resolve** `registry.json` — official org (`noxs-pkg`) first, then
   the requested GitHub repository.
2. **Version pick** — latest, or the exact `@version` requested.
3. **Architecture detect** — `aarch64`, `x86_64`, `armv7`; a
   `universal` asset is used for architecture-independent packages.
4. **Download** — streamed, retried, resumable; prefers the
   [mirror](../architecture/mirror.md) (sha256-keyed cache, hits are
   reported), falls back to the official URL.
5. **Verify** — SHA-256 against `registry.json` **and** the published
   `.sha256` sidecar. Mismatched artifacts are never installed.
6. **Member-check** — every archive entry is checked for path
   traversal / absolute paths / absolute symlinks before extraction.
7. **Extract** at the environment root and record an installed-package
   manifest.

## Progress and output

Interactive terminals render one live line:

```
Downloading curl_…arm64.deb  67%  4.8/7.2 MB  2.1 MB/s  ETA 2s
```

computed from real bytes and elapsed time (unknown sizes show bytes and
speed, never an invented percentage). Non-interactive terminals and CI
get a plain transcript; `--json` keeps stdout machine-readable with
diagnostics on stderr.

## Removal and listing

```console
noxs@ubuntu:~$ nx list           # installed packages (Ubuntu + Noxs)
noxs@ubuntu:~$ nx info tree      # details for one package
noxs@ubuntu:~$ nx remove tree    # asks for confirmation
```

Removal touches only files recorded in the package manifest (under
`usr/` or `opt/`) — never Noxs itself, never apt's database.

## Errors

Stable error codes (machine-readable with `--json`): `PACKAGE_NOT_FOUND`,
`UNSUPPORTED_ARCHITECTURE`, `NETWORK_ERROR`, `DOWNLOAD_FAILED`,
`CHECKSUM_MISMATCH`, `SIGNATURE_VERIFICATION_FAILED`,
`DEPENDENCY_RESOLUTION_FAILED`, `INSUFFICIENT_DISK_SPACE`,
`INSTALL_PERMISSION_DENIED`, `PACKAGE_MANAGER_BUSY`, `MIRROR_UNAVAILABLE`.
The full table with causes and fixes lives in
[Troubleshooting](package-troubleshooting.md).

`nx install <name>` delegates to the apt flow when the name is not a
Git-registry package (disable the fallback with
`NOXS_INSTALL_FALLBACK=0`) — see
[Linux package management](../environments/linux-package-management.md).
