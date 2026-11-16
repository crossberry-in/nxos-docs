# Shell Configuration

Noxs sessions run **bash** as the `noxs` user with home `/home/noxs`.
The shell is the environment's own `/bin/bash` — no custom Noxs shell
sits in between.

## Login environment

| Item | Value |
|---|---|
| Shell | `/bin/bash` (login shell, `-l`) |
| User / group | `noxs` |
| Home | `/home/noxs` |
| Working directory | `/home/noxs` |
| `NOXS` | `1` |
| `NOXS_VERSION` | the app version |
| `TERM` | the terminal's TERM value |
| `LANG` | `C.UTF-8` |

Sessions launch through `su -s /bin/bash -l noxs` under proot's
fake-root, so the login files apply normally.

## Startup files

Standard bash semantics apply:

| File | Read | Use it for |
|---|---|---|
| `/etc/profile` + `/etc/profile.d/*` | login shells | system-wide defaults |
| `~/.profile` | login shells | per-user env (PATH, locale) |
| `~/.bashrc` | interactive shells | prompt, aliases, functions |

The rootfs is provisioned with standard Ubuntu dotfiles. Add your
aliases to `~/.bashrc`:

```console
noxs@ubuntu:~$ cat >> ~/.bashrc <<'EOF'
alias ll='ls -alF'
export EDITOR=nano
EOF
noxs@ubuntu:~$ exec bash -l
```

## The prompt

The installer sets the prompt identity `noxs@ubuntu` (host part comes
from the environment's terminal profile — the legacy Debian import keeps
its own `noxs@android` identity). Customize freely in `~/.bashrc`:

```console
noxs@ubuntu:~$ export PS1='\u@\h:\w\$ '
```

## Password and sudo

The `noxs` password is collected once during setup and used by `sudo`
inside the environment. It is never stored by the app and never
transmitted. To change it:

```console
noxs@ubuntu:~$ passwd
```

## Sessions and shells

Sessions, keep-alive and restore behavior are controlled from the
terminal settings — see [Sessions](sessions.md). Nothing in the shell
configuration is overwritten by app updates: dotfiles live in your
rootfs and survive upgrades.
