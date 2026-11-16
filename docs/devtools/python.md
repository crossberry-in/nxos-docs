# Python

Python 3 is not part of the minimal base rootfs — Noxs installs it
on demand when a feature needs it (for example the
[`nx ai`](../ai/nx-ai.md) runtime), and you can install it explicitly:

## Install

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y python3 python3-pip python3-venv
noxs@ubuntu:~$ python3 --version
```

*(Ubuntu 24.04 ships Python 3.12.x — `apt policy python3` shows the
exact candidate.)*

## Using pip and venv

```console
noxs@ubuntu:~$ python3 -m venv ~/venvs/demo
noxs@ubuntu:~$ . ~/venvs/demo/bin/activate
(demo) noxs@ubuntu:~$ pip install requests
```

Prefer venvs over system-wide pip installs; Ubuntu's `pip` refuses
system installs outside venvs by design (PEP 668).

## Python package projects with the NX system

```console
noxs@ubuntu:~$ nx pkg init mylib --python
noxs@ubuntu:~$ cd mylib && nx pkg build
```

The template ships `pyproject.toml`, a `src/main.py` entry and GitHub
Actions release automation that publishes a universal artifact — see
[Development workflows](workflows.md).

## The AI agent runtime

The [`nx ai`](../ai/nx-ai.md) agent is Python (stdlib only) and
auto-installs `python3` with the same honest progress pattern as the
package system if it is missing:

```
nx: Installing dependencies... (python3)
```

## Notes

- `pip install` of packages with native extensions requires
  `build-essential`.
- Wheels for `linux-aarch64` are widely available on PyPI; source
  builds fall back to the compiler toolchain.
- There is no conda/pyenv preconfigured; version management via apt is
  the supported path.
