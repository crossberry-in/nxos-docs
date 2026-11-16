# Package Updates

Keeping packages and the environment current — three layers, three
commands.

## NX packages

```console
noxs@ubuntu:~$ nx update            # update all installed NX packages
noxs@ubuntu:~$ nx update tree       # update one package
```

- `nx update <package>` refreshes the package's registry, compares the
  installed version with `latest` and installs the newer release with
  the same verify-then-extract pipeline as
  [`nx install`](package-install.md).
- Without a package name every installed NX package is processed.
- `nx pkg update [--full]` is the distro-front-end variant:
  by default it refreshes package indexes; `--full` runs the actual
  upgrade.

## Ubuntu packages (apt)

```console
noxs@ubuntu:~$ noxs update          # apt metadata refresh + upgrade
noxs@ubuntu:~$ sudo apt update && sudo apt upgrade
```

`noxs update` runs `apt-get update` and then a non-interactive
upgrade through the native apt engine. See
[Linux package management](../environments/linux-package-management.md).

## What updates touch

| Layer | Updated by | Where it lands |
|---|---|---|
| NX packages | `nx update` / `nx pkg update` | Environment root, tracked by the package manifest |
| Ubuntu packages | `noxs update` / `sudo apt upgrade` | Rootfs, tracked by dpkg |
| code-server | `noxs code install` (re-run) | `/opt/code-server` |

## Cloud package versions are immutable

Published NXMirror Cloud versions never change — an update always
resolves to a **new** version. See
[Package registry](package-registry.md).

## Staying current

- Run `nx pkg update` after long offline periods.
- `nx pkg doctor` reports when the package index is empty (`apt-cache
  policy` does not respond) and points to the refresh command.
- Release notes for the app itself live in the
  [Changelog](../changelog.md).
