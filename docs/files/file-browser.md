# File Browser

Noxs has two complementary file surfaces:

1. **The Noxs file browser** (in-app) — opened with `noxs files` from
   the terminal or from the app's navigation.
2. **The system Files app entry "Noxs Linux Home"** — any
   DocumentsUI-compatible picker can browse the guest home.

## Opening the browser

```console
noxs@ubuntu:~$ noxs files
```

The bridge request opens the Noxs file browser activity on the Android
side; the command prints nothing on success. The browser operates on
the guest filesystem through the same editor filesystem layer the
DocumentsProvider uses — one mapping, consistent behavior.

## The "Noxs Linux Home" root

The [documents provider](../android/internal-storage.md) exposes
`/home/noxs` of the active environment. The system Files app shows it
as:

```
Noxs Linux Home
Ubuntu 24.04 guest files
```

Capabilities: browse, open, edit (write-through to the Linux files),
create files and folders, rename, delete. The root itself can never be
deleted or renamed through SAF.

## Refresh behavior

- Children cursors notify their observers, so open pickers refresh
  when files change.
- After an environment switch, install or reset, the provider asks
  DocumentsUI to re-query roots — a stale "Noxs Linux Home" entry
  should not persist. If it does, see
  [Troubleshooting → Storage](../troubleshooting/storage-errors.md).

## Choosing between the surfaces

| Task | Best surface |
|---|---|
| Quick copy to/from Android folders | [SAF storage commands](../android/storage-permissions.md) |
| Save into another app's location | [`noxs document export`](../android/file-picker.md) |
| Visual browsing of the guest home | This browser / Files app |
| Editor with a full workspace | [Code Server](../devtools/code-server.md) |
