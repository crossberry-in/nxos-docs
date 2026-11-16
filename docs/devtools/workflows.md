# Development Workflows

Two supported loops cover most work: **local development** (apt
toolchains + the editor) and **package publishing** (NX templates +
GitHub Actions or NXMirror Cloud).

## Loop 1 — local development

```console
noxs@ubuntu:~$ sudo apt install -y git build-essential python3
noxs@ubuntu:~$ mkdir ~/projects && cd ~/projects
noxs@ubuntu:~$ git clone https://github.com/user/repo.git && cd repo
noxs@ubuntu:~$ # edit with code-server or a terminal editor
noxs@ubuntu:~$ noxs code start        # editor at 127.0.0.1:8080
noxs@ubuntu:~$ make && ./run-tests.sh
noxs@ubuntu:~$ git add . && git commit -m "wip" && git push
```

The editor's workspace follows your terminal's `cd` (OSC 7) — see
[Code Server](code-server.md).

## Loop 2 — build and publish a package

### 1. Scaffold

```console
noxs@ubuntu:~$ nx pkg init mytool --rust     # or --node --cpp --python --go
```

creates:

```
mytool/
├── .github/workflows/pkg.yml   # build + release automation (multi-arch)
├── src/main.{js,rs,cpp,py}     # or main.go + go.mod (Go)
├── package.json | Cargo.toml | CMakeLists.txt | pyproject.toml | go.mod
├── registry.json               # release metadata (updated automatically)
├── VERSION                     # 1.0.0 — read by CI
├── README.md
└── LICENSE
```

### 2. Implement + verify locally

```console
noxs@ubuntu:~$ cd mytool
noxs@ubuntu:~$ nx pkg build       # runs npm / cargo / cmake / pip / go build
noxs@ubuntu:~$ nx pkg release     # pre-flight: VERSION, registry, tag checks
```

### 3a. Publish via GitHub

```console
noxs@ubuntu:~$ git add . && git commit -m "release: mytool 1.0.0" && git push
```

GitHub Actions then: detects the language → validates VERSION →
rejects duplicate tags → multi-arch build → package + sha256 → tags
`mytool-v1.0.0` → GitHub Release with `.nx.pkg` assets → updates
`registry.json` → commits it with `[skip ci]`.

Anyone can then install:

```console
noxs@ubuntu:~$ nx install mytool
```

### 3b. Publish to NXMirror Cloud

```console
noxs@ubuntu:~$ nxc register        # once
noxs@ubuntu:~$ nx pkg deploy       # build + upload the current package
```

Direct CLI uploads are limited to **4 MiB per artifact**; cloud
versions are immutable and store the artifact URL, size and SHA-256 —
see [Package registry](../packages/package-registry.md).

## Choosing languages

| Flag | Template | Release artifacts |
|---|---|---|
| `--node` (`--nodejs`) | npm + `src/main.js` | universal |
| `--rust` | Cargo + `src/main.rs` | x86_64 · aarch64 · armv7 |
| `--cpp` (`--c++`) | CMake + `src/main.cpp` | x86_64 · aarch64 · armv7 |
| `--python` (`--py`) | pyproject + `src/main.py` | universal |
| `--go` | go.mod + `main.go` | x86_64 · aarch64 · armv7 |

Running `nx pkg init <name>` without a flag opens the interactive
keyboard selector.
