# File Upload and Download

"Upload" and "download" in Noxs mean moving files between the Linux
sandbox and Android (or the wider device). Four verified paths exist.

## 1. Document import/export (picker-based)

```console
noxs@ubuntu:~$ noxs document import downloads    # Android → ~/<dir>
noxs@ubuntu:~$ noxs document export ~/hello.txt  # sandbox → any Android location
```

Progress + cancel on import; the system save dialog on export. See
[File picker](../android/file-picker.md).

## 2. SAF category get/put (folder-mapped)

```console
noxs@ubuntu:~$ noxs storage get downloads report.pdf ~/report.pdf
noxs@ubuntu:~$ noxs storage put shared notes.txt notes.txt
```

`get` copies a document **into** the sandbox; `put` copies a sandbox
file **out** into the mapped folder. See
[Storage permissions](../android/storage-permissions.md).

## 3. Direct /sdcard mount (opt-in, POSIX-style)

```console
noxs@ubuntu:~$ cp ~/report.pdf ~/storage/downloads/report.pdf
```

Requires the two-step opt-in — see
[External SD card](../android/external-sdcard.md).

## 4. Share sheet

```console
noxs@ubuntu:~$ noxs share ~/report.pdf          # hand a file to any Android app
noxs@ubuntu:~$ noxs share -t "build finished"   # share text
```

The Android Sharesheet decides the destination (chat, Drive, email…).
From other apps, Android's *Share to…* and *Save to Noxs Linux Home*
flows write into the guest home through the documents provider.

## Choosing a path

| Situation | Use |
|---|---|
| One-off file, any location | `document import` / `export` |
| Regular work with specific folders | `storage get/put` |
| Heavy shell workflows (many files) | direct mount (opt-in) |
| Sending to a person/app | `noxs share` |

## Moving archives and backups

Archives produced inside the sandbox (see
[Archive management](archive-management.md)) leave the device with
`noxs document export <archive>` or `noxs share <archive>` — the same
path recommended for [environment backups](../environments/backup-restore.md).
