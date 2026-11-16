# File Operations

Create, copy, move, rename and delete — inside the sandbox with
ordinary Linux commands, and across the SAF boundary with Noxs storage
commands.

## Inside the sandbox (POSIX)

```console
noxs@ubuntu:~$ mkdir -p src/tests
noxs@ubuntu:~$ cp a.txt b.txt
noxs@ubuntu:~$ mv b.txt src/
noxs@ubuntu:~$ rm src/b.txt
```

Everything under `/` (the guest rootfs) behaves like a real Linux
filesystem, including permissions and symlinks. Files you create in
`/home/noxs` are visible to Android through
[Noxs Linux Home](file-browser.md).

## Through SAF (command-based)

```console
noxs@ubuntu:~$ noxs storage mkdir shared reports
noxs@ubuntu:~$ noxs storage cp shared a.txt shared/reports/a.txt
noxs@ubuntu:~$ noxs storage mv shared reports/a.txt shared/a.txt
noxs@ubuntu:~$ noxs storage rm shared old.txt
noxs@ubuntu:~$ noxs storage cat shared/notes.txt
```

- Operations apply **within one selected folder tree** per category.
- `rm` deletes through Android's document provider — real deletion,
  always explicit.
- `cat` reads a document to the terminal.

## From the Files app / browser

The Noxs file browser and the system Files app support create, rename,
delete and edit for [Noxs Linux Home](file-browser.md); name changes
are sanitized (no separators, no `..`, collision-safe numbering) by the
provider's policy layer.

## Editor operations

The built-in editor (code-server) exposes the full VS Code file
operations over its workspace — with write-through to the real guest
files. See [Code Server](../devtools/code-server.md).

## Deleting safely

- `noxs storage reset` / `revoke` release **mappings only** — they
  never delete your files.
- Guest-side `rm` is ordinary Linux `rm`; there is no trash service in
  the sandbox — double-check before deleting shared-storage paths under
  the opt-in mount.
