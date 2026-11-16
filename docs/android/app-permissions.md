# Android App Permissions and the Permission Center

The Permission Center is the central authority behind every privileged
Noxs API request (Noxs API spec §6-§10). This page documents both the
**real Android permissions** the app can use and the **Noxs permission
ids** that gate package/plugin APIs.

    Application
       ↓
    Permission Center          (ui/PermissionCenterActivity.kt)
       ↓
    Permission Manager         (runtime/NoxsPermissionCenter.kt)
       ↓
    Android / Noxs Runtime
       ↓
    API authorization

## Principles

- Every privileged API request passes permission validation — no exceptions.
- Packages are never trusted because they are installed.
- WebView JavaScript is never trusted by default.
- Only the minimum permissions required are requested.
- Android permission state is never faked: the center probes the real OS
  state (`ContextCompat`/`PackageManager`) and never claims access until
  Android confirms it.
- Special Android access opens the appropriate Android settings screen and
  verifies the resulting state afterwards.

## Permission levels and states (spec §8)

Levels: `required` · `optional` · `feature-dependent`

States: `Allowed` · `Not granted` · `Denied` · `Restricted` · `Not supported`

An absent decision means NOT granted. `feature-dependent` permissions map
to real feature toggles (for example `background.keepawake` follows the
Settings → Background switch).

## Permission catalog

Groups (spec §9): Notifications · Storage / Files · Background activity ·
Device features · System integration · Noxs environment access

| group       | ids                                                              |
|-------------|------------------------------------------------------------------|
| notifications | notifications.show (POST_NOTIFICATIONS)                        |
| storage     | storage.read, storage.write (SAF picker — never all-files access)|
| background  | background.tasks (FOREGROUND_SERVICE), background.keepawake (WAKE_LOCK) |
| device      | device.vibrate                                                   |
| system      | window.create, window.control, web.open, web.control             |
| environment | terminal.read/subscribe/write/execute, logs.read/subscribe, storage.package, package.read/install, system.info |
| android     | android.media, android.camera, android.sms.send, android.storage.mount — see below |

Default package access is read/subscribe only. `terminal.write` and
`terminal.execute` are NEVER granted automatically (spec §13) — execution
always requires an explicit user decision.

## The Network row

Ordinary Internet access is NOT presented as an Android runtime permission
(spec §9). It is enabled through the application's normal network
capability and shown as informational status only:

    Network
    ✓ Available
    Internet access is enabled for Noxs.

## First-launch flow (spec §9)

    Noxs Launch
      → Permission Center
      → detect required permissions
      → show status (search + groups)
      → user grants/denies
      → verify (each pending Android permission asked at most once per session)
      → environment setup
      → Noxs Home

The flow runs once (flag `permission_onboarding_done` in noxs_settings);
the Permission Center stays permanently available in Settings →
Permissions. Denied permissions stay honest as "Not granted" — they are
never silently hidden.

## NX Android Integration permissions

The Android-bridge capabilities have their own catalog entries
(`runtime/NoxsPermissionCatalog.kt`):

| id | Android backing | Behavior |
|---|---|---|
| `android.media` | `READ_MEDIA_IMAGES` (API 33+, asked on use) | Import photos/videos through the Photo Picker or SAF |
| `android.camera` | `android.permission.CAMERA` (runtime grant) | Open the native camera for `noxs camera`; captures reach the terminal only after capture |
| `android.sms.send` | **none — no Android SMS permission** | Hands the message to *your own* SMS app; you press send there. Never automatic, never bulk |
| `android.storage.mount` | Android's All-files-access Settings screen | OPT-IN direct shared-storage mount (`/sdcard` in the guest); default off; revocable any time |

## Storage and real Android permissions

- storage.read/write use the SAF document-tree picker (existing
  StorageActivity flow); Noxs never requests all-files access for them.
- POST_NOTIFICATIONS is the notifications runtime permission in the
  current catalog and is requested on API 33+ only, through the real
  Android API.
- CAMERA is requested at first use of a camera flow.
- WAKE_LOCK / FOREGROUND_SERVICE / VIBRATE are install-time permissions;
  the center reflects the actual OS answer via the probe.
- The direct-mount opt-in is special: it opens Android's own Settings
  screen (`MANAGE_ALL_FILES_ACCESS_PERMISSION`) and verifies the
  resulting state after you return — see
  [External storage](external-sdcard.md).

State persists as `noxs-permissions.json` inside the app sandbox with a
tamper guard: unknown ids never survive a load.

## Android permission model in one page

| Permission | When it is requested | Scope |
|---|---|---|
| `POST_NOTIFICATIONS` (33+) | First notification / on `noxs notification permission` | Progress + user notifications |
| `CAMERA` | First `noxs camera` / gallery-with-camera use | Captures only, handed back as a file |
| `READ_MEDIA_IMAGES` (33+) | First media import | Scoped media access |
| `MANAGE_EXTERNAL_STORAGE` | Only via the explicit direct-mount opt-in | Shared storage bind — off by default |
| SAF folder grants | Every `noxs storage setup/map` | Selected folders only |
| **SMS (send/read/contacts)** | **Never** — sending goes through your own SMS app | — |
