# Linux Package Management (APT)

Inside the environment, packages are managed with the **native apt
engine** and official Ubuntu repositories. Noxs never replaces or
re-signs apt metadata.

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y git curl python3
noxs@ubuntu:~$ sudo apt upgrade
noxs@ubuntu:~$ apt search <name>
noxs@ubuntu:~$ apt show <name>
```

## How Noxs layers on top

| Layer | Command | What it adds |
|---|---|---|
| Native apt | `sudo apt …` | The real Ubuntu flow, full dependency resolution |
| Distro front end | `nx pkg search/install/info/list/remove/update/doctor` | Merged view of apt + NX packages, live progress UI, signed-hash re-verification of every `.deb` |
| NX packages | `nx install <name>` | Git-based `.nx.pkg` releases — see [NX Package System](../packages/package-manager.md) |

`nx pkg install <name>` resolves the file list, sizes and SHA-256
hashes from the **signed** repository metadata (`apt-get --print-uris`),
re-verifies every downloaded `.deb` against that hash before
`apt-get install` runs, and prefers the [download
mirror](../architecture/mirror.md) as a cache accelerator with automatic
fallback to the official URL. Nothing is ever installed
unauthenticated.

## Environment refresh helpers

```console
noxs@ubuntu:~$ noxs update      # apt metadata refresh + upgrade
noxs@ubuntu:~$ nx pkg update    # refresh package indexes (--full runs the upgrade)
```

`noxs update` runs `apt-get update` and then a non-interactive upgrade
through native apt.

## Health and repair

```console
noxs@ubuntu:~$ nx pkg doctor
```

checks: distro identity, apt sources, keyring, dpkg database, CA
certificates, download tools, free storage. Warnings print the matching
repair command (usually [`nx cert-fix`](../cli/cert-fix.md)).

## What belongs to which package store

- **apt**: everything from Ubuntu repositories — installed into the
  rootfs, tracked by dpkg.
- **NX packages** (`nx install`): tracked in a separate installed-package
  manifest under `usr/` or `opt/`; removal only touches files recorded
  in that manifest.

The two stores are independent; `nx pkg list` shows both.
