# Root Filesystem Management

The root filesystem (rootfs) is the guest's entire Linux tree. It lives
in app-private storage and is managed by the app — you normally never
touch the host-side paths, only the guest paths through the terminal.

## Layout

```
<app filesDir>/noxs/                 (or environments/<id>/ for registry installs)
├── rootfs/                          the guest / (Ubuntu tree)
│   ├── home/noxs/                   your home (exposed as "Noxs Linux Home")
│   ├── etc/noxs/resources.conf      resource quotas (app-managed)
│   └── var/run/noxs/                runtime control dirs (host-bound)
├── run/                             app-side control directories
└── .noxs-installed-v1               install marker (distro + suite)
```

## Health checks

```console
noxs@ubuntu:~$ noxs status          # environment health summary
noxs@ubuntu:~$ noxs ubuntu status   # identity, repos, keyring, package index
noxs@ubuntu:~$ nx pkg doctor        # package-layer deep check
```

`nx pkg doctor` validates Ubuntu identity, repositories, keyring, dpkg
database state, certificates, download tools and free storage, printing
`OK` / `WARN` rows with the matching repair hint.

## Automatic repairs

- **Interrupted dpkg configuration** is detected and repaired on
  startup (the setup console shows "Checking for interrupted dpkg
  configuration").
- **dpkg status database corruption** (truncated `status`, broken
  `status`/`status-old` links) is repaired from the alternate copy when
  possible.
- **Missing `/home/noxs`** is recreated (empty) by the documents
  provider so the Files entry never silently vanishes — see
  [File browser](../files/file-browser.md).

## Resizing and usage figures

The app walks the rootfs (skipping symlinks) to report disk usage in the
terminal's resource widget; figures are TTL-cached for 15 seconds and
are invalidated when an environment is removed. Guest-created symlinks
never leak foreign storage into the usage figure.

## Reset and reinstall

- A **reset** removes the environment's rootfs and lets setup run again
  from scratch (explicit user action in the app).
- **Removal** of an environment deletes its storage path — other
  environments are untouched (see
  [Environment switching](environment-switching.md)).

## Backups

User data can be exported to a `tar.gz` archive and restored later —
see [Backup and restore](backup-restore.md). The archive covers the
home directory plus Noxs control files, not the whole rootfs.
