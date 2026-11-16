# Git

Git is not preinstalled; install it from the official repositories:

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y git
noxs@ubuntu:~$ git --version
```

## Everyday use

```console
noxs@ubuntu:~$ git config --global user.name "Your Name"
noxs@ubuntu:~$ git config --global user.email "you@example.com"
noxs@ubuntu:~$ git init && git add . && git commit -m "first"
```

Cloning over HTTPS works out of the box (certificates come from
`ca-certificates`; repair with [`nx cert-fix`](../cli/cert-fix.md) if a
network repair ever broke them).

## SSH remotes

SSH-based remotes need `openssh-client` and your key setup — see
[SSH](ssh.md) for the verified client workflow.

## NXMirror Git Cloud

`nx git` opens the NXMirror Git Cloud web interface in the Noxs browser
window; `nxc` (the NXMirror CLI) handles `register`, `login`,
`whoami`, `packages` and `pkg deploy` — see
[Package registry](../packages/package-registry.md).

## Git in the package workflow

`nx pkg init` runs `git init` in the new project when the directory is
not already a repository, and the release flow is commit-driven:

```console
noxs@ubuntu:~$ cd mytool
noxs@ubuntu:~$ git add . && git commit -m "release: mytool 1.0.0" && git push
```

GitHub Actions then builds, tags and publishes — see
[Development workflows](workflows.md).

## Editors for commit messages

Set a terminal-friendly editor for interactive commits:

```console
noxs@ubuntu:~$ git config --global core.editor nano
```
