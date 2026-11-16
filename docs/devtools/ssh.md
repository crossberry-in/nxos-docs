# SSH

SSH **client** workflows are fully supported in the terminal. Running
an SSH **server** inside the sandbox is possible as an ordinary guest
process, but is not something Noxs exposes to your network by design.

## Client install and basics

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y openssh-client
noxs@ubuntu:~$ ssh user@example.com
noxs@ubuntu:~$ scp file.tar.gz user@example.com:/tmp/
```

## Key-based authentication

```console
noxs@ubuntu:~$ ssh-keygen -t ed25519
noxs@ubuntu:~$ ssh-copy-id user@example.com
```

Keys live under `~/.ssh/` in the guest home. Because the home is part
of the sandbox, keys are private to your device; keep backups of
public keys wherever you register them.

## Git over SSH

```console
noxs@ubuntu:~$ sudo apt install -y git
noxs@ubuntu:~$ git clone git@github.com:user/repo.git
```

First connections write `known_hosts` normally.

## Running an SSH server (advanced, sandbox-scoped)

`openssh-server` installs and runs as a guest process:

```console
noxs@ubuntu:~$ sudo apt install -y openssh-server
```

Honest limits to understand before you rely on it:

- The server binds inside the **sandbox**; it is reachable only from
  the device itself unless you deliberately expose the port with a
  tunnel — Noxs never forwards ports automatically.
- proot environments do not provide the isolation guarantees of a
  dedicated device — see the
  [security model](../architecture/security.md) before treating a
  guest-side SSH daemon as a hardened endpoint.
- Noxs makes no guarantees about the server surviving session or
  device restarts; services are guest processes (see
  [`noxs-service`](../cli/noxs.md#services-and-sockets)).

## Troubleshooting

- Connection failures are usually network/transport issues — check
  `noxs network status`.
- Certificate/known-host errors after repairs: see
  [Certificates & APT repair](../cli/cert-fix.md).
