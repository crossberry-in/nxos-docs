# Directory Navigation

Navigation inside the sandbox is ordinary Linux navigation — plus a few
Noxs-specific touches.

## Terminal navigation

```console
noxs@ubuntu:~$ pwd
/home/noxs
noxs@ubuntu:~$ ls -la
noxs@ubuntu:~$ mkdir projects && cd projects
```

Your home is `/home/noxs`; every session starts there. Standard shell
navigation (`cd`, `pushd`, tab completion, `~` expansion) works as on a
real computer.

## Where things live

| Path | Contents |
|---|---|
| `/home/noxs` | Your files (exposed to Android as *Noxs Linux Home*) |
| `~/storage/*` | Direct-mount links to shared storage (opt-in) — see [External SD card](../android/external-sdcard.md) |
| `~/imports` | Default landing of `noxs document import` |
| `~/.noxs/plugins/<id>/` | Installed plugins |
| `~/.noxs/code/` | code-server data |
| `/var/run/noxs/` | Runtime control dirs (host-bound) — do not delete |

## Editor follows the terminal

The built-in editor attaches to your current working directory: the
shell publishes its location via **OSC 7**, and the code-server
workspace follows the active terminal session. `cd` in the terminal,
open the editor — it opens where you are. See
[Code Server](../devtools/code-server.md).

## Files app navigation

In the system Files app, *Noxs Linux Home* lists guest folders first,
then files, both sorted case-insensitively. The provider re-sorts on
refresh; hidden dotfolders are visible (they are part of your home).

## SAF folders are not POSIX paths

Folders mapped through
[storage commands](../android/storage-permissions.md) are accessed by
category, not by `cd`:

```console
noxs@ubuntu:~$ noxs storage ls downloads
noxs@ubuntu:~$ noxs storage get downloads report.pdf ~/report.pdf
```

A direct `cd` works only in the opt-in `/sdcard` mount — see
[External SD card](../android/external-sdcard.md).
