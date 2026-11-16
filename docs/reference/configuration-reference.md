# Configuration Reference

Noxs persists settings in app-private storage. This page lists the
verified keys and files; everything else lives in code defaults.

## Terminal settings (`noxs_settings`, `terminal.*`)

| Key | Range / values | Default |
|---|---|---|
| `terminal.fontSize` | 10–28 sp | example toolbar shows `A− 14 A+` |
| `terminal.fontFamily` | font family | system default |
| `terminal.lineSpacing` / `terminal.letterSpacing` | spacing factors | default |
| `terminal.cursorStyle` | block / underline / bar | block |
| `terminal.cursorBlink` / `terminal.cursorBlinkPeriod` | on/off; 200–1500 ms | on |
| `terminal.cursorWidth` | 1–4 | 1 |
| `terminal.padding` | 0–24 dp | default |
| `terminal.opacity` | 50–100 % | 100 |
| `terminal.theme` | Noxs Dark / Black / High contrast / Paper | Noxs Dark |
| `terminal.pinchZoom` / `terminal.twoFingerScroll` | on/off | on / off |
| `terminal.selectionEnabled` / `terminal.autoScrollSelection` | on/off | on |
| `terminal.hapticFeedback` | on/off | on |
| `terminal.showToolbar` / `terminal.showExtraKeys` | on/off | on |
| `terminal.scrollMode` | normal / smart / history-mirror | smart |
| `terminal.followLiveOutput` / `terminal.showNewOutputIndicator` / `terminal.autoFollowWhileRunning` | on/off | on |
| `terminal.scrollbackLines` | 1,000–50,000 | 10,000 |
| `terminal.confirmExit` | on/off | off |
| `terminal.keepAlive` / `terminal.restoreSessions` | on/off | — |
| `terminal.autoFocusTerminal` / `terminal.preserveScrollPosition` | on/off | — |
| `terminal.reduceAnimations` / `terminal.textAntialias` / `terminal.debugOverlay` | on/off | — |
| `terminal.startFullscreen` | on/off | off |

Values are clamped at load and save; the terminal reset removes only
`terminal.*` keys.

## AI configuration (`~/.noxs/ai/config.json`)

Full key table: [AI configuration](../ai/configuration.md). Environment
overrides: `NOXS_AI_PROVIDER`, `NOXS_AI_MODEL`, `NOXS_AI_BASE_URL`,
`NOXS_AI_API_KEY_ENV` (+ `NOXS_AI_API_KEY` fallback key variable).

## Storage-related settings

| Setting | Where |
|---|---|
| Direct /sdcard mount toggle | SharedPreferences `noxs_android_bridge`, key `direct_mount` — see [External storage](../android/external-sdcard.md) |
| SAF folder mappings | persisted URI grants, managed by `noxs storage repair|reset|revoke` |
| Permission decisions | `noxs-permissions.json` (tamper-guarded; unknown ids dropped) |

## Download cache

| Path | Contents |
|---|---|
| `~/.noxs/cache/pkg/deb/<sha256>.deb` | sha256-keyed `.deb` cache |
| `~/.noxs/cache/pkg` | package download cache root |

## Package CLI environment variables

| Variable | Effect |
|---|---|
| `NOXS_PKG_MIRROR` | Mirror base URL (`off` disables the mirror) |
| `NOXS_PKG_REQUIRE_MIRROR=1` | Fail instead of degrading when the mirror is unreachable |
| `NOXS_INSTALL_FALLBACK=0` | Stop `nx install` falling through to apt |
