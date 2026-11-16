# Android File Picker and File Import/Export

The document bridge moves files between Android and the Linux sandbox
through Android's own picker UIs. Every transfer is explicit: Android
shows the picker and you choose exactly which document(s) Noxs may
touch. No storage permission is needed for these flows.

## Command reference

```console
noxs@ubuntu:~$ noxs document
Usage: noxs document [command]
  open                 Pick an Android document and open it in an Android app
  import [dir] [--type MIME]
                       Import one or more Android documents into ~/<dir>
                       (default: ~/imports) with progress and cancel
  export <file> [name] [mime]
                       Export a Noxs file to any Android location through
                       the system save dialog
  gallery [dest-file]  Pick a photo through the Android Photo Picker and
                       save it inside Noxs
  picker [dest-file]   Pick one Android document and save it inside Noxs
```

## Importing files into the sandbox

```console
noxs@ubuntu:~$ noxs document import          # → ~/imports
noxs@ubuntu:~$ noxs document import demo     # → ~/demo
noxs@ubuntu:~$ noxs document import demo --type image/png
```

Multi-select import with progress and cancel. The `--type` filter
narrows the picker to a MIME type.

## Exporting files out of the sandbox

```console
noxs@ubuntu:~$ echo hello > ~/hello.txt
noxs@ubuntu:~$ noxs document export ~/hello.txt
noxs@ubuntu:~$ noxs document export ~/hello.txt hello-backup.txt text/plain
```

The system save dialog lets you choose any Android location (Downloads,
Drive, …). Name and MIME are optional — the file's basename and
detected MIME type are used by default.

## One-shot picks

```console
noxs@ubuntu:~$ noxs document picker          # one document → ~/picked-<timestamp>
noxs@ubuntu:~$ noxs document open            # hand a document to an Android app
```

## Transfers over the bridge

Imports and exports stream through the file-based bridge
(`/var/run/noxs/host/android`) with response payloads — the same
validated transport every bridge command uses. Large files stream
without being loaded whole into memory.

## Related

- [Storage commands](storage-permissions.md) — SAF categories with
  `get`/`put` for folder-mapped access.
- [Gallery and camera](gallery.md) — Photo Picker and camera captures.
- [File upload/download](../files/upload-download.md) — the same flows
  from the file manager's point of view.
