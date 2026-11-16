# Ubuntu Configuration

After [installation](ubuntu-installation.md) the environment is
pre-configured. This page documents what exists and how to inspect or
adjust it.

## Identity and defaults

| Item | Value |
|---|---|
| Prompt | `noxs@ubuntu:~$` |
| User | `noxs` (uid from the Noxs passwd database, `sudo` group member) |
| Home | `/home/noxs` |
| Locale | `C.UTF-8` |
| PATH | `/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin` |
| Environment flag | `NOXS=1`, `NOXS_VERSION=<app version>` |

## APT repositories (official Ubuntu only)

`/etc/apt/sources.list.d/noxs.sources` is a deb822 file written by the
installer:

- **arm64 / armhf**: `ports.ubuntu.com/ubuntu-ports` — suites `noble`,
  `noble-updates`, `noble-backports`, `noble-security`; components
  `main restricted universe multiverse`;
  `Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg`.
- **amd64**: `archive.ubuntu.com/ubuntu` + `security.ubuntu.com/ubuntu`,
  same suites and components.

Inspect it with:

```console
noxs@ubuntu:~$ cat /etc/apt/sources.list.d/noxs.sources
```

Do not add unsigned third-party repositories; if a mirror or key breaks,
[nx cert-fix](../cli/cert-fix.md) restores the official file.

## Inspecting the environment

```console
noxs@ubuntu:~$ noxs ubuntu status
```

reports: pretty name, version, codename, kernel (Android host kernel via
proot), architecture, shell, apt source host, keyring presence and
whether the package index responds.

```console
noxs@ubuntu:~$ noxs status        # environment health summary
noxs@ubuntu:~$ nx pkg doctor      # package-layer health check
```

## DNS, hostname and resources

- `/etc/resolv.conf` is written by Noxs at configuration time (the stock
  ubuntu-base file ships empty).
- The hostname and `/etc/hosts` are configured during userspace setup.
- Resource quotas (CPU, memory pressure, process caps) are applied
  through `/etc/noxs/resources.conf`, bound read-only into the guest by
  proot — see [Bootstrap system](../architecture/bootstrap.md).

## Time zone, locale and shell customization

Ubuntu base ships `C.UTF-8`. You can install additional locales with
apt (`locales` package) and set time zone data via `tzdata`. Shell
prompt, aliases and environment belong in `~/.bashrc` — see
[Shell configuration](../terminal/shell-configuration.md).

## What NOT to change

- The proot bind points under `/var/run/noxs` (they are real directories
  inside the rootfs that the app reads) — see
  [Unix domain sockets](../architecture/unix-sockets.md).
- `/etc/noxs/resources.conf` (managed by the app).
- The `noxs` user entry: the terminal session and the Android editor
  assume it.
