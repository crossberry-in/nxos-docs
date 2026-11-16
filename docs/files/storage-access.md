# Storage Access

This page summarizes **every** storage access path Noxs can use, what
each requires and what it can reach. Details live in the linked pages.

## The complete map

| Path | Mode | Android permission | Page |
|---|---|---|---|
| `/home/noxs` (guest home) | App-private storage | none (own sandbox) | [Internal storage](../android/internal-storage.md) |
| SAF categories (`shared`, `downloads`, `dcim`, `pictures`, `music`, `movies`) | Command-based (`noxs storage ls/get/put/…`) | none — user-picked folders | [Storage permissions](../android/storage-permissions.md) |
| `/sdcard` + `~/storage/*` | proot bind, POSIX-style | All-files access + explicit `mount` opt-in | [External SD card](../android/external-sdcard.md) |
| Photo Picker / document picker | Bridge, per-selection grants | none (picker) | [File picker](../android/file-picker.md) |
| Camera captures | Bridge | `CAMERA` on first use | [Gallery](../android/gallery.md) |
| MicroSD card | Via SAF categories | none — user-picked folder | [External SD card](../android/external-sdcard.md) |

## Defaults are the narrow path

- Fresh installs hold **no** storage permission beyond the app sandbox.
- Nothing is requested at startup; each capability asks when used.
- The direct `/sdcard` mount is off by default and needs **two**
  explicit user actions (Android's Settings screen + `noxs storage
  mount`).

## Capacity and status reporting

```console
noxs@ubuntu:~$ noxs storage list      # locations, capacity, selected folders, mount
noxs@ubuntu:~$ noxs device storage    # non-identifying storage report
```

Reports are summaries — no identifiers. See
[Device reports](../cli/noxs.md#android-bridge-commands).

## What storage access can NOT do

- It cannot read another app's private storage.
- It cannot touch Android system partitions.
- SAF grants cover exactly the folders you picked — nothing more.
- Revoking grants in Android Settings immediately degrades the
  corresponding commands to honest errors.
