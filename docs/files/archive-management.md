# Archive Management

Archives appear in two places in Noxs: tools **you** run inside the
guest, and the hardened extraction the app itself uses during
installation.

## Working with archives in the terminal

Ubuntu 24.04 ships the standard tooling; install extras with apt:

```console
noxs@ubuntu:~$ sudo apt install -y unzip zip xz-utils
noxs@ubuntu:~$ tar -czf project.tar.gz project/
noxs@ubuntu:~$ tar -xzf project.tar.gz
noxs@ubuntu:~$ unzip code.zip -d code/
noxs@ubuntu:~$ xz -d big.tar.xz
```

A guest-created archive can leave the device with
`noxs document export <archive>` or `noxs share <archive>` — see
[File upload and download](upload-download.md).

## TarGuard — the app-side safe extractor

Everything the **app** extracts (the Ubuntu rootfs, code-server
downloads, plugin artifacts) goes through TarGuard, the hardened
extraction layer shared by the installer pipeline:

- rejects `..` traversal, absolute paths, drive letters and NUL bytes;
- rejects escaping symlinks/hardlinks, device and FIFO entries;
- strips setuid/setgid bits;
- caps total extracted size;
- verified entry counts stream into the setup console.

The same member-checks protect NX package installs
(`.nx.pkg` tarballs) — see the
[package security model](../packages/package-manager.md#security-model).

## Migration backups are archives too

Legacy-Debian → Ubuntu data migration produces
`debian-home-backup-<utc>.tar.gz` archives inside the guest; restoring
is a plain `tar -xzf` — see
[Backup and restore](../environments/backup-restore.md).

## Guest-created archives and Android

Archives inside your home are visible to Android through
[Noxs Linux Home](file-browser.md); extract *outside* the home (e.g.
`/tmp`) when testing untrusted files so the home stays clean:

```console
noxs@ubuntu:~$ mkdir /tmp/unpack && tar -xzf untrusted.tar.gz -C /tmp/unpack
```
