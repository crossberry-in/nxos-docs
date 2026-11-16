# Kali Configuration — Planned

!!! warning "Status: planned — not available in the current release"
    There is no Kali environment to configure yet. This page describes
    the **planned** configuration surface so it can be reviewed before
    the track ships. Everything here mirrors how the Ubuntu
    environment is configured today — see
    [Ubuntu configuration](ubuntu-configuration.md).

## Planned configuration areas

| Area | Planned behavior |
|---|---|
| APT sources | Official Kali repositories over HTTPS, `Signed-By` keyring file, deb822 format — written by the installer, restorable with `nx cert-fix` |
| Locale | `C.UTF-8` default, installable via apt |
| User | `noxs` user with home `/home/noxs`, `sudo` group member, password set in the setup console |
| Prompt | `noxs@kali:~$` |
| DNS | Written by Noxs at configuration time |
| Resources | The same `/etc/noxs/resources.conf` quota mechanism as Ubuntu |

## Status and health commands (environment-independent)

These commands exist today and will report Kali identity once the
environment exists:

```console
noxs@ubuntu:~$ noxs status     # environment health summary
noxs@ubuntu:~$ nx pkg doctor   # identity, repos, keyring, dpkg, certs, space
```

## Certificates and APT repair

The [`nx cert-fix`](../cli/cert-fix.md) repair flow (signed-HTTP
bootstrap, CA bundle regeneration, curl/wget provisioning) is
apt-family-aware and is planned to cover the Kali sources file the same
way it covers Ubuntu's `noxs.sources` today.

## Common questions

**Can I rename/convert the Ubuntu environment into Kali?**
No. Environments are distinct installs; conversion is not planned.

**Will legacy Debian environments become Kali?**
No — legacy imports stay read-only
([Environment switching](environment-switching.md)).
