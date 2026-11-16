# Quick Start

Ten minutes from a fresh install to a productive terminal. All examples
assume the Ubuntu 24.04 environment and the `noxs@ubuntu:~$` prompt.

## 1. Check the environment

```console
noxs@ubuntu:~$ noxs status
noxs@ubuntu:~$ noxs ubuntu status
```

`noxs status` prints the environment health summary; `noxs ubuntu
status` prints the Ubuntu identity (os-release, codename, arch, apt
sources, keyring, package index). If apt sources or certificates show
`WARN`, run `nx cert-fix` — see
[Certificates & APT repair](../cli/cert-fix.md).

## 2. Refresh package metadata

```console
noxs@ubuntu:~$ apt update
```

APT is the native Ubuntu engine with official repositories —
[Linux package management](../environments/linux-package-management.md)
has the details.

## 3. Install your first tools

```console
noxs@ubuntu:~$ sudo apt install -y git curl
```

## 4. Try the NX Package System

```console
noxs@ubuntu:~$ nx install tree
noxs@ubuntu:~$ tree --help | head -3
```

`nx install` resolves a package's `registry.json`, verifies the SHA-256
and extracts it — see [NX Package System](../packages/package-manager.md).

## 5. Open the editor (optional)

```console
noxs@ubuntu:~$ noxs code install     # one-time download of code-server
noxs@ubuntu:~$ noxs code start       # binds 127.0.0.1:8080 only
```

The Noxs editor screen attaches to the same server automatically. See
[Code Server](../devtools/code-server.md).

## 6. Meet the Android bridge

```console
noxs@ubuntu:~$ noxs help             # every Noxs command
noxs@ubuntu:~$ noxs document import  # pull files in through Android's picker
noxs@ubuntu:~$ noxs files            # open the Noxs file browser (Android UI)
```

Each capability asks through Android's own UI the first time — see
[Android Integration](../android/overview.md).

## 7. Keep going

- [Terminal interface](../terminal/terminal-interface.md) — gestures,
  search, scroll modes, settings.
- [NX command system](../cli/nx.md) — the full `nx` / `noxs` command
  map.
- [AI Agent Terminal](../ai/nx-ai.md) — `nx ai` for a tool-using agent.
- [Plugin Store](../plugins/plugin-sdk.md) — `nx plug` to browse
  plugins.

!!! note "Prompts in examples"
    Example output on this site shows *realistic* sessions, not captured
    device transcripts — your version strings, timings and file names
    will differ.
