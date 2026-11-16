# Package Initialization — `nx pkg init`

`nx pkg init <name> [--<language>]` creates a new package project from
a Noxs language template. The scaffold carries everything needed for
automated releases: source entry, build config, release workflow,
registry and version files.

## Syntax

```console
noxs@ubuntu:~$ nx pkg init <package-name> [--node|--rust|--cpp|--python|--go]
```

- Names are validated: lowercase letters, digits, `.`, `-`, `_`;
  must start with a letter or digit. Invalid names are rejected with
  `Invalid package name: <name> …`.
- The target directory must not already exist.
- Without a language flag an interactive, keyboard-navigable selector
  opens (Node.js / Rust / C++ / Python / Go); without a terminal
  attached it asks you to pass a flag explicitly.

## What is created

```
<name>/
├── .github/workflows/pkg.yml   # build + release automation (multi-arch)
├── src/main.{js,rs,cpp,py}     # or main.go + go.mod at the root (Go)
├── package.json | Cargo.toml | CMakeLists.txt | pyproject.toml | go.mod
├── registry.json               # release metadata, updated automatically
├── VERSION                     # 1.0.0 — semantic version, read by CI
├── README.md
└── LICENSE
```

- The `__PKG_NAME__` placeholder in template files is replaced with
  your package name.
- `git init` runs automatically when the parent directory is not
  already inside a repository.
- Templates live under
  `/usr/local/share/noxs-pkg/templates/<language>/files` — adding a
  language later means adding a directory; the package manager does
  not need to change (see
  [extending the system](package-manager.md#extending)).

## After init

```console
noxs@ubuntu:~$ cd <name>
noxs@ubuntu:~$ # 1. implement in src/
noxs@ubuntu:~$ nx pkg build
noxs@ubuntu:~$ nx pkg release          # pre-flight validation
noxs@ubuntu:~$ git add . && git commit -m "release: <name> $(cat VERSION)" && git push
```

Then either push to GitHub (Actions publishes the release) or publish
to NXMirror Cloud with `nx pkg deploy` — both flows are documented in
[Development workflows](../devtools/workflows.md).

## Errors

| Message | Meaning |
|---|---|
| `Invalid package name: …` | Name violates the character rules |
| `Directory already exists: <name>` | Target path exists |
| `Only one package name is allowed` | Extra positional arguments were passed |
| `Unsupported language: <lang>` | Unknown language flag |
| `Cancelled — no package was created.` | Selector aborted; nothing was written |
