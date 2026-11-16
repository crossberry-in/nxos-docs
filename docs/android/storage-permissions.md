# Storage Permissions

Noxs is SAF-first: shared storage access is granted per-folder through
Android's Storage Access Framework, is command-based in the terminal,
and is never an all-files grant by default. A separate, clearly-labeled
opt-in enables a direct `/sdcard` mount — see
[External SD card / direct mount](external-sdcard.md).

## The two modes

1. **SAF mode (default, always available)** — you pick folders with
   Android's own picker; access goes through `noxs storage …`
   commands. Never a POSIX path, never an all-files grant.
2. **Direct mount (opt-in)** — `noxs storage mount` **plus** Android's
   user-granted *All files access* (`noxs storage grant --direct`).
   Both are required; either can be revoked at any time.

## Storage command reference

```console
noxs@ubuntu:~$ noxs storage
Usage: noxs storage [command]
  status                         Show current user-granted folder access
  setup                          Choose a shared folder with Android's picker
  map <category>                 Choose a folder for a category
  repair                         Re-check persisted permissions and mappings
  reset                          Release Noxs mappings only (never deletes files)
  ls <category> [relative-path]  List documents inside a selected folder
  mkdir <category> <path>        Create a folder through the SAF provider
  cat <category> <path>          Read a document to the terminal
  get <category> <path> <local>  Copy a document into the Noxs Linux sandbox
  put <category> <path> <local>  Copy a sandbox file into the selected folder
  rm <category> <path>           Delete the selected document via Android's provider
  cp <category> <src> <dest>     Copy within one selected folder tree
  mv <category> <src> <dest>     Move within one selected folder tree
  permission                     Android permission + mount overview
  grant [--direct]               Pick a SAF folder (--direct: Android's
                                 all-files-access screen for the /sdcard mount)
  revoke                         Release all Noxs storage grants
  mount                          Opt in to the direct /sdcard bind for NEW
                                 sessions + create ~/storage/* links
  unmount                        Opt out of the direct /sdcard bind
  list                           Locations, capacity, selected folders, mount

Categories: shared, downloads, dcim, pictures, music, movies
```

`noxs storage permission` prints the Android permission overview plus
the mount status; `noxs storage list` adds locations, capacity and the
selected folders.

## Examples

```console
noxs@ubuntu:~$ noxs storage setup        # Android folder picker opens
noxs@ubuntu:~$ noxs storage ls downloads
noxs@ubuntu:~$ noxs storage get downloads report.pdf ~/report.pdf
noxs@ubuntu:~$ noxs storage put shared notes.txt notes.txt
```

## What the app requests

- **SAF flows request nothing.** The picker hands a document/folder URI
  to Noxs; Android persists the grant.
- The **direct mount** requires Android's *All files access* (a
  Settings screen, not a runtime dialog) **and** the explicit
  `noxs storage mount` toggle.
- On Android 13+, media import flows may use the scoped
  `READ_MEDIA_*` permissions when a feature needs them — asked on use,
  never at startup. See
  [App permissions](app-permissions.md#nx-android-integration-permissions).

## Revocation

- `noxs storage revoke` — releases all Noxs SAF mappings.
- `noxs storage unmount` — turns the direct mount off.
- Android Settings → Permissions — the underlying grants are Android's
  own and remain user-controlled; status commands report honestly after
  a revocation.

## Notes and limits

- SAF access is **command-based, not a POSIX mount** — you cannot `cd`
  into a SAF-granted folder; use `ls/get/put/…`.
- Removal/reset never deletes your files: it releases Noxs mappings
  only.
- Bridge ids and control directories are validated and symlink-hardened;
  paths are checked before use.
