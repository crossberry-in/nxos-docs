# Permission Errors

Noxs never fakes permission state — the Permission Center probes the
real Android answer and surfaces one of: `Allowed` · `Not granted` ·
`Denied` · `Restricted` · `Not supported`. This page maps the states to
repairs. The full catalog:
[App permissions](../android/app-permissions.md).

## "Not granted" / "Denied"

| Feature | Repair |
|---|---|
| Notifications (API 33+) | `noxs notification permission` or Android Settings → Apps → Noxs → Notifications |
| Camera | Open a camera flow (`noxs camera`) — Android asks on use; grant there |
| Media import (API 33+) | Grant the scoped media prompt when it appears |
| SAF folders | `noxs storage setup` / `map <category>` |
| Direct mount | `noxs storage grant --direct` **and** `noxs storage mount` |

Denied permissions stay visible as "Not granted" — they are never
silently hidden.

## "Restricted"

The feature's toggle is off (feature-dependent permissions follow their
feature switch, e.g. `background.keepawake` follows the Settings →
Background switch). Enable the feature in the app.

## "Not supported"

The Android version does not implement the permission the way the
catalog entry expects (e.g. POST_NOTIFICATIONS below API 33) — the
feature degrades honestly instead of erroring.

## Bridge command says "unavailable"

UI-backed bridge operations (pickers, camera, confirmations) run in
the foreground activity. Keep Noxs open for those steps and retry:

```console
noxs@ubuntu:~$ noxs sms contacts
Contact selection cancelled
```

A cancelled picker is **not** an error — nothing was granted, nothing
was read.

## After revoking in Android Settings

- Status commands report honestly on next use.
- SAF mappings keep their persisted grants until revoked; `noxs
  storage repair` re-checks them.
- The direct mount stops applying to new sessions once All-files
  access is revoked.

## Package/plugin permission denials

Packages get `Denied` for anything the user has not granted;
`terminal.write` / `terminal.execute` are **never** granted
automatically — see
[Permission Center](../android/app-permissions.md#principles).

## "groups: cannot find name for group ID 3003 / 9997 / ..."

**What it is:** cosmetic, expected output inside proot environments.

**Why it appears:** the guest process inherits Android's kernel-level
supplementary groups — `3003` (`inet`, network access), `9997`
(`everybody`) and device-specific ids such as `20803`/`50803`. Those GIDs
exist on Android's side, not in the Ubuntu `/etc/group`, so when a tool
resolves group names (`groups`, `id`) the lookup prints this note. proot
fakes the uid via ptrace but supplementary groups pass through unchanged.

**What Noxs does:** no arbitrary group assignments, no modified
permission semantics — the notes are informational only, and genuine
permission errors still surface normally. `noxs info` prints a short
explanation of this in the environment overview.

**What NOT to do:** do not add fake `/etc/group` entries for Android
GIDs and do not try to drop the groups — neither improves security or
behavior, and hiding real permission errors would be worse than the
cosmetic note.
