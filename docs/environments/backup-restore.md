# Environment Backup and Restore

Noxs does not (yet) ship a generic "backup everything" button. What
exists today is a **verified migration backup** that captures your user
data into a `tar.gz` archive so files survive an environment
transition — primarily the legacy-Debian → Ubuntu migration.

## What the backup covers

The migration planner scopes entries that actually exist on your
install:

| Entry | Contents |
|---|---|
| `home/noxs` | Your entire guest home directory |
| `root` | The guest root account's home |
| `etc/noxs/resources.conf` | App-managed resource quota file |

The archive is named `debian-home-backup-<utc-timestamp>.tar.gz` and is
written to app-private storage under `files/noxs/migration/`. The
timestamp makes repeated migrations non-destructive — each run produces
a new archive instead of overwriting the old one.

## How the backup is produced

The archive is created **inside the guest** by a one-shot proot run of
`tar -czf`, with the migration directory bind-mounted at
`/noxs-backup`. Only existing entries are included; an install with
nothing to back up produces no archive and reports that honestly.

## Restoring into Ubuntu

After the Ubuntu environment is installed, restore from the terminal:

```console
noxs@ubuntu:~$ # the archive must be reachable inside the guest first —
noxs@ubuntu:~$ # e.g. copy it into the home with the Android bridge:
noxs@ubuntu:~$ noxs document import .
noxs@ubuntu:~$ tar -xzf debian-home-backup-20260101T0000Z.tar.gz -C ~ --strip-components=2  # adjust paths
```

!!! warning "Check the archive layout before extracting"
    `tar -t` the archive first and pick the right `-C` /
    `--strip-components` so files land in `~` rather than nested
    directories. A restore merges into your current home and can
    overwrite same-named files.

## Recommendations

1. **Back up before major transitions** — installing Ubuntu over a
   legacy install, or running a reset.
2. **Copy archives off-device** — `noxs document export <archive>` or
   `noxs share <archive>` hands the file to Android; store it in Drive
   or wherever you keep backups.
3. **APT-installed packages are not in the backup** — reinstall them
   with `sudo apt install …` after a restore.

## Related

- [Migration and legacy environments](environment-switching.md)
- [Rootfs management](rootfs-management.md)
- [File import and export](../android/file-picker.md) for moving
  archives in and out of the sandbox.
