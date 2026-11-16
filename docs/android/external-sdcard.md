# External SD Card and the /sdcard Mount

"External storage" on Android means shared storage
(`/storage/emulated/0` — what most people call *internal SD* on phones,
plus the physical microSD card when present). Noxs accesses it in two
honest ways, both user-controlled.

## SAF categories (default)

`noxs storage` works with six categories: `shared`, `downloads`, `dcim`,
`pictures`, `music`, `movies`. You map each category to a real folder
with Android's own picker (`noxs storage setup` / `map`), then use the
command-based API — see
[Storage permissions](storage-permissions.md#storage-command-reference).
This mode needs **no all-files grant**.

## The direct /sdcard mount (opt-in)

For terminal-native workflows Noxs can bind shared storage into the
guest as a real POSIX tree:

```
/storage/emulated/0  →  /sdcard            (proot bind, read-write)
~/storage/shared     →  /sdcard            (Termux-style links)
~/storage/downloads  →  /sdcard/Download
~/storage/dcim       →  /sdcard/DCIM
~/storage/pictures   →  /sdcard/Pictures
~/storage/music      →  /sdcard/Music
~/storage/movies     →  /sdcard/Movies
```

### Enabling it — two explicit actions

```console
noxs@ubuntu:~$ noxs storage grant --direct   # opens Android's All-files-access screen
noxs@ubuntu:~$ noxs storage mount            # toggles the mount + creates ~/storage links
```

1. **Android's own Settings screen** must grant *All files access*
   (`MANAGE_EXTERNAL_STORAGE`) — Noxs cannot grant this to itself.
2. **`noxs storage mount`** turns the Noxs toggle on; it persists across
   terminal restarts and applies to **new sessions** (already-running
   sessions don't gain the bind).

`noxs storage unmount` turns it off; `noxs storage status` reports
both switches honestly:

```
Direct shared-storage mount
Android grant: all-files access granted | not granted
Noxs toggle:   on | off
Mount:         /storage/emulated/0 -> /sdcard (active for new sessions)
```

### Using it

```console
noxs@ubuntu:~$ noxs storage mount
noxs@ubuntu:~$ # start a NEW terminal session, then:
noxs@ubuntu:~$ ls ~/storage/shared
noxs@ubuntu:~$ ls /sdcard/Download
```

### Notes and limits

- Creating `/sdcard` inside the guest **never** grants storage access
  by itself — only the two user actions above do, and Noxs reports
  exactly which one is missing.
- Without the grant, no bind is added and the guest sees no `/sdcard`
  path (Noxs does not pretend otherwise).
- The mount exposes the device's shared storage to the guest — treat
  guest commands accordingly; `rm` under `/sdcard` is real.
- Revocation from Android Settings takes effect on the next session;
  status commands keep reporting honestly afterwards.

## Physical microSD cards

Writable microSD paths are device-specific; the SAF categories remain
the reliable interface — map the `shared` category to a folder on the
card with `noxs storage setup`.
