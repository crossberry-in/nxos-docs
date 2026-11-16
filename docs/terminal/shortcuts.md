# Terminal Shortcuts and Keyboard Support

## Shortcut-key row

The row above the keyboard offers `ESC TAB CTRL ↑ ↓ ← →` (and related
keys). Visibility is controlled by the **Show shortcut keys** setting
(`terminal.showExtraKeys`), and the whole toolbar can be hidden with
`terminal.showToolbar`.

## Full screen

`Ctrl+F` — or the toolbar menu's *Full screen* / *Exit full screen* —
toggles an immersive terminal: status bar, session tabs, action toolbar
and shortcut-key row hide, and system bars hide (swipe to reveal
transiently). The state persists across rotation and process death; the
shell keeps running.

## Toolbar

`↑ ↓ Copy Paste Search A− 14 A+ ⋮` — the `⋮` menu offers clear
scrollback, save/share output, reset font size and terminal settings.
Tap the size label to reset the font size.

## Touch gestures

| Gesture | Action | Notes |
|---|---|---|
| Single-finger drag | Scroll history | fling with physics |
| Long press | Text selection | draggable handles, edge auto-scroll, Share |
| Two fingers apart / together | Font size − / + | pinch, 10–28 sp, snapped to 0.5 sp |
| Two-finger drag | Scroll history | optional setting, off by default |

Priority: selection handles > long-press selection > pinch >
two-finger scroll > normal scroll. Touches never send shell input.

## Hardware keyboards

Noxs works with external keyboards through the standard Android input
path: Ctrl key combinations (e.g. `Ctrl+C`, `Ctrl+D`, `Ctrl+F`), arrow
keys and function-driven UI shortcuts behave like a desktop terminal.
Terminal-specific rendering (cursor, colors) follows the active
[terminal theme](customization.md#appearance).

## Search in the terminal

The toolbar **Search** opens a case-insensitive search over the full
document (scrollback + screen) with an `n/m` counter and ↑/↓ navigation
with wraparound. Search is a pure buffer read — the shell input stream
is never written and running programs are never interrupted.
