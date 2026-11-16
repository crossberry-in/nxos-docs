# Notifications

The terminal can post Android notifications through the bridge — used
for long-running tasks (installs, downloads, environment setup) and for
notifications you explicitly trigger from the command line.

## Command reference

```console
noxs@ubuntu:~$ noxs notification status      # capability summary
noxs@ubuntu:~$ noxs notification permission  # request POST_NOTIFICATIONS (Android 13+)
noxs@ubuntu:~$ noxs notification post "Build done" "tests passed in 42s"
```

- `status` — reports whether notifications are permitted and the
  channel state. No private data is read.
- `permission` — triggers Android's own permission prompt on Android
  13+ (`POST_NOTIFICATIONS`); on older versions it is a no-op.
- `post <title> [body...]` — posts a notification with your title and
  body. Everything after the title becomes the body text.

## Background progress

While installs or downloads run in the background, a progress
notification keeps the task visible — that flow is managed by the app
itself; see [Background execution](background-execution.md) and
[Activity Center](background-execution.md).

## Notes

- Notification text comes from you (or the app's task progress); the
  bridge never reads message stores or private data.
- Notifications are revocable in Android Settings at any time; `status`
  reports the honest state afterwards.
