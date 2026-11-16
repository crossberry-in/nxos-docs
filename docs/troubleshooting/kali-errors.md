# Kali Errors

!!! warning "Status: planned — no Kali environment exists yet"
    Noxs ships **Ubuntu 24.04 LTS** only
    ([Kali status](../environments/kali-installation.md)). There are no
    Kali-specific errors to troubleshoot today, because there is no
    Kali download, no Kali provider and no Kali rootfs in the current
    release.

## If you were expecting Kali

- The distribution is not selectable in the current app — installs run
  the Ubuntu pipeline.
- Do **not** hand-extract a Kali rootfs into the app's private
  storage; that path is unsupported and will be replaced by the
  official installer when the track ships.

## apt-family errors in general

Kali is apt-based; the generic repair flows documented for Ubuntu
apply to any future apt environment:

- [Ubuntu errors](ubuntu-errors.md)
- [`nx cert-fix`](../cli/cert-fix.md) — sources + CA repair
- [Package errors](package-errors.md)

## Watch this page

When the Kali track ships, this page will list its real error modes
(download verification, keyring, sources) with verified fixes.
