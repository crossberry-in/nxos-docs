# Internal Storage (Noxs Linux Home)

Noxs's Linux files live in the app's private storage. They are exposed
to Android through a documents provider named **Noxs Linux Home**, so
any DocumentsUI-compatible app — the system Files app, editors, "Save
to…" dialogs — can browse, open, edit, create, rename and delete files
that really live in the Noxs Linux filesystem.

## What is exposed

Exactly one root: **`Noxs Linux Home` → `/home/noxs`** of the active
environment. Nothing else — never the whole rootfs, never `/data/data`,
never another app's storage. The summary line shows the guest
("Ubuntu 24.04 guest files").

## How it works

```
System Files app (DocumentsUI)
      │  Storage Access Framework
      ▼
NoxsDocumentsProvider  ── policy: home-only allowlist, traversal and
      │                    symlink-escape rejection, name sanitization
      ▼
/home/noxs  (direct java.io/nio access — the same mapping the editor
             and plugin installer use)
```

- `openDocument` hands out real file descriptors — edits write through
  to the Linux files, never to a temporary copy; large files stream.
- Children/roots cursors notify observers, so open pickers refresh
  when files change.
- If `/home/noxs` is missing (reset, interrupted migration), the
  provider recreates an **empty** home rather than letting the Files
  entry vanish; a reset never destroys data through this path.

## Using it

1. Open any app's file picker (or the system Files app).
2. Choose **Noxs Linux Home**.
3. Browse `/home/noxs` — folders first, then files; create, rename and
   delete where flags allow (the root itself cannot be deleted or
   renamed).

From the terminal, `noxs files` opens the Noxs file browser UI — see
[File browser](../files/file-browser.md).

## Folders created by features

| Path | Created by |
|---|---|
| `~/storage/*` | The opt-in direct mount links — see [External storage](external-sdcard.md) |
| `~/imports/` | Default destination of `noxs document import` |
| `~/Pictures/` | Default destination of `noxs camera` and gallery picks |
| `~/.noxs/` | App data: AI config, code-server data, installed plugins (`~/.noxs/plugins/<id>/`) |

## Security properties

- Document ids are absolute guest paths validated against traversal,
  control characters and symlink escapes; every path must resolve
  **inside** `/home/noxs`.
- Display names from the system UI are sanitized (no separators, no
  hidden-file tricks, collision-safe numbering).
- The provider requests no permissions — the documents are the app's
  own sandbox files.

!!! tip "Files not showing in the picker?"
    The root serves the **active environment**. After switching
    environments, give the Files app a refresh; the provider notifies
    roots on environment changes. See
    [Troubleshooting → Storage](../troubleshooting/storage-errors.md).
