# Package Troubleshooting

## Health check first

```console
noxs@ubuntu:~$ nx pkg doctor
```

validates distro identity, repositories, keyring, dpkg database,
certificates, download tools and free storage, printing `OK`/`WARN`
rows with the matching repair hint.

## Stable error codes

`--json` output and logs use these codes; the CLI prints a user-facing
message and never stack traces or internal paths.

| Code | Meaning | Typical fix |
|---|---|---|
| `PACKAGE_NOT_FOUND` | No such package in any source | Check spelling; `nx pkg search <name>` |
| `UNSUPPORTED_ARCHITECTURE` | No asset for this device arch | Look for a `universal` release or an aarch64 asset |
| `NETWORK_ERROR` | Could not reach any source | `noxs network status`; retry |
| `DOWNLOAD_FAILED` | Transfer failed mid-way | Retry — downloads resume (`-C -` on the second attempt) |
| `CHECKSUM_MISMATCH` | sha256 differs from registry/sidecar | The artifact is broken — never installed; report it to the package author |
| `SIGNATURE_VERIFICATION_FAILED` | apt signature check failed | [`nx cert-fix`](../cli/cert-fix.md); check the repo keyring |
| `DEPENDENCY_RESOLUTION_FAILED` | apt could not resolve deps | `sudo apt update`; check third-party sources |
| `INSUFFICIENT_DISK_SPACE` | Not enough free space | Free space; `df -h /` in the guest |
| `INSTALL_PERMISSION_DENIED` | Installation blocked | Check `sudo` works; see [Permission errors](../troubleshooting/permission-errors.md) |
| `PACKAGE_MANAGER_BUSY` | Another package op is running | Wait — operations are single-flight locked |
| `MIRROR_UNAVAILABLE` | Mirror down **and** required | Use official sources (default) or unset `NOXS_PKG_REQUIRE_MIRROR` |

## Common situations

**`apt-get update` fails with certificate errors** — run
[`nx cert-fix`](../cli/cert-fix.md); it rebuilds the CA bundle and
repairs the sources file.

**`Release already exists: <name>-v<version>`** — the tag was already
published; bump `VERSION` and release again.

**Cache behavior** — downloads are cached in `~/.noxs/cache/pkg`
keyed by SHA-256; cache hits are reported as such. A corrupt cache
entry can be deleted by hand; verification happens before every
install regardless.

**The mirror is slow/down** — nothing to do by default: the installer
falls back to official URLs automatically. See
[mirror architecture](../architecture/mirror.md).

**Where to ask** — open an issue at
<https://github.com/crossberry-in/noxs/issues> with the error code and
the command you ran.
