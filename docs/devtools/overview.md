# Developer Tools Overview

The environment is a full Ubuntu 24.04 userspace, so the standard
toolchains are one `apt install` away. This section documents the
verified workflows; anything requiring extra setup is stated explicitly.

## What is already there

| Tool | Status |
|---|---|
| bash, coreutils, tar/gzip/xz | Included in the base rootfs |
| apt / dpkg | Native, official repositories |
| sudo | Password-protected, sandbox-scoped |
| `noxs`, `nx`, `nxc` CLIs | Preinstalled |
| curl / wget | Provided by `nx cert-fix` (also installable via apt) |
| git, python3, build-essential, nodejs, npm, rustc, g++ | **Install via apt** (see the section pages) |

## Installing a toolchain

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y build-essential git curl
```

apt keeps everything tracked and upgradeable — see
[Linux package management](../environments/linux-package-management.md).

## Ready-made project scaffolding

`nx pkg init <name> --<language>` creates a project with language
template, build config and GitHub Actions release automation for
**Node.js, Rust, C++, Python and Go** — see
[Development workflows](workflows.md) and
[Package initialization](../packages/package-manager.md#for-package-authors).

## The editor

The built-in editor is real code-server (VS Code in the browser),
local-only with a workspace that follows your terminal — see
[Code Server](code-server.md).

## Remote work

SSH clients (`openssh-client`) install via apt; running an SSH *server*
inside the sandbox is a normal guest process bound to the sandbox —
see [SSH](ssh.md) for the honest capability picture.

## Performance

Native compilation works, but the device CPU and thermals are the
ceiling. Heavy builds benefit from the
[Rust performance core](../architecture/rust-core.md) paths Noxs uses
internally and from keeping parallel jobs modest (`make -j2`).
