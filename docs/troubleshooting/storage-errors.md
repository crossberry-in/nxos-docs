# Storage Errors

## `noxs storage ls …` says nothing is mapped

SAF access needs a picked folder first:

```console
noxs@ubuntu:~$ noxs storage setup      # or: map <category>
noxs@ubuntu:~$ noxs storage repair     # re-check persisted grants
```

If Android revoked the grant (Settings or a "reset app permissions"
action), `repair` reports it and `setup` re-grants.

## `cd /sdcard` fails: "No such file or directory"

That path exists **only** with the opt-in direct mount — and only in
**new sessions**:

1. `noxs storage grant --direct` — approve All-files access in
   Android's Settings screen.
2. `noxs storage mount` — create the `~/storage/*` links too.
3. Start a **new** terminal session; `ls /sdcard` and
   `ls ~/storage/shared` now work.

`noxs storage status` tells you exactly which step is missing. See
[External SD card](../android/external-sdcard.md).

## `~/storage/*` links exist but listing fails

The links are created by `noxs storage mount`; they resolve only while
the mount conditions hold (grant + toggle + a new session). After a
revocation they hang harmlessly — `noxs storage unmount` removes the
state cleanly and `mount` recreates it.

## Files app shows "Noxs Linux Home" empty or stale

- The root serves the **active environment's** `/home/noxs` — check
  which environment is active.
- The provider re-creates an empty home if it was missing and asks
  DocumentsUI to refresh; if the entry stays stale, close and reopen
  the Files app.
- Files created in the terminal appear immediately; files created
  while the picker was open trigger a child-notification refresh.

## `noxs storage put/get` fails mid-transfer

- Check free space in both places (`noxs storage list` shows
  capacity).
- Bridge timeouts report "did not respond" — keep Noxs in the
  foreground for picker/camera/confirm flows; background transfers do
  not need it. Retry the command.

## Permission overview seems wrong after revoking in Android

Status commands probe the real OS state and never fake answers — after
a revocation they report the honest "not granted" state. Run
`noxs storage permission` to confirm; see
[Permission errors](permission-errors.md).
