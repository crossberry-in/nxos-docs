# Terminal Customization

Everything on this page lives in **Settings → Terminal** in the app,
persists to the `noxs_settings` file under `terminal.*` keys and
applies live. The full key list is in the
[Configuration reference](../reference/configuration-reference.md).

## Appearance

Font size (10–28 sp), font family, line spacing, letter spacing, cursor
style (block/underline/bar), cursor blink on/off + period
(200–1500 ms), cursor width (1–4), padding (0–24 dp), opacity
(50–100 %) and the terminal theme:

- **Noxs Dark** (default)
- **Black** (OLED)
- **High contrast**
- **Paper** (light)

The site itself follows your device's light/dark preference via the
theme toggle in the header.

## Interaction

Pinch zoom, two-finger scrolling, long-press selection, auto-scroll
selection, haptic feedback, toolbar visibility and shortcut-key row
visibility.

## Scrolling

Scroll mode (**Normal / Smart / History Mirror**), follow live output,
new-output indicator, auto-follow while running, scrollback size
(1,000–50,000 lines).

## Behavior

Confirm exit (off by default), keep sessions alive in background,
restore previous sessions, auto-focus terminal, preserve scroll
position.

## Advanced

Reduce animations, smooth text rendering, debug details.

## Reset

The reset action removes **only** `terminal.*` keys, after
confirmation. The Linux filesystem, packages, shell history, sessions
and user files are never touched.

## Values are clamped

Every stored value is clamped at load and save; invalid stored values
can never reach the terminal engine.
