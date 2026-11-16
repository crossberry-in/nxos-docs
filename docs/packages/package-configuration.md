# Package Configuration

A NX package is configured through a handful of files. Everything here
is verified against the package templates; nothing else is required.

## VERSION

A plain text file holding the semantic version (`1.0.0`), read by the
release workflow. Invalid versions are rejected at release time.
Bump it for every release — the workflow refuses to overwrite existing
tags (`Release already exists: <name>-v<version>`).

## registry.json

Release metadata, **maintained automatically** by the release
workflow — the schema and rules live in
[Package registry](package-registry.md). Do not hand-edit release
entries.

## Build configuration

Per language, the template ships the standard build file:

| Language | File | Build tool (`nx pkg build`) |
|---|---|---|
| Node.js | `package.json` | `npm` |
| Rust | `Cargo.toml` | `cargo` |
| C++ | `CMakeLists.txt` | `cmake` |
| Python | `pyproject.toml` | `pip` |
| Go | `go.mod` | `go build` |

The workflow fails cleanly when a build tool is missing.

## template.conf (language authors)

Language templates live under
`/usr/local/share/noxs-pkg/templates/<language>/` with a
`template.conf` (language id, display name, supported architectures,
build system) and a `files/` tree. Adding a language means adding a
directory — see [extending](package-manager.md#extending).

## GitHub Actions workflow

`.github/workflows/pkg.yml` (generated) owns the release pipeline:

```
checkout → detect language → validate VERSION → reject duplicate tags
        → multi-architecture build → package + sha256
        → tag <name>-v<version> → GitHub Release with .nx.pkg assets
        → update registry.json (preserve versions, bump latest)
        → commit registry.json [skip ci]
```

Architecture matrix: Go/Rust/C++ build `x86_64`, `aarch64`, `armv7`
(Go natively; Rust/C++ via cross toolchains). Node.js/Python publish a
single `universal` artifact.

## CLI-side configuration

| Setting | Where | Effect |
|---|---|---|
| Download cache | `~/.noxs/cache/pkg` | sha256-keyed `.deb` cache; hits reported |
| Mirror endpoint | `NOXS_PKG_MIRROR` | Override/disable the mirror (`off` disables) |
| Git fallback | `NOXS_INSTALL_FALLBACK=0` | Stop `nx install` falling through to apt |
| Required mirror | `NOXS_PKG_REQUIRE_MIRROR=1` | Fail instead of degrading when the mirror is down |
