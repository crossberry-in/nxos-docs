# Terminal Performance

The terminal is designed for steady 60 fps-class rendering on mid-range
ARM64 devices. These notes describe the implemented engineering choices
(see the source under `terminal-view/` and `terminal-emulator/`).

## Renderer

- Paint objects are reused; nothing is allocated per frame.
- Smooth text rendering is optional (`terminal.textAntialias`) for
  low-end devices.
- Reduce animations (`terminal.reduceAnimations`) trims non-essential
  motion.

## Scrollback

- Fixed-capacity ring buffer: O(1) row lookup at any configured size.
- Independent from the shell process; clearing it never disturbs
  running programs.
- Resize is live (`resizeScrollback`); shrinking keeps the newest rows.

## Search

Search highlights are binary-sliced per visible window instead of
scanning the whole buffer per frame.

## Setup console

- Spinner ticks at ~10 Hz only while the setup console is visible.
- Elapsed text updates at 1 Hz under a monotonic clock.
- Live lines are rewritten in place (`CR` + `EL`) and clamped to the
  real column count — below 24 columns the console falls back to
  `frame elapsed` only.

## Input

- Pinch zoom applies font size in 0.5 sp steps so PTY resizes stay
  rare.
- Preference writes are `apply()` (async), one per user action.

## The heavier paths

For sustained compute, use the right tool:

| Workload | Where to read more |
|---|---|
| Native-speed file hashing/extraction | [Rust performance core](../architecture/rust-core.md) |
| Editors and language servers | [Code Server](../devtools/code-server.md) |
| Resource quotas (CPU/RAM) | [Bootstrap system](../architecture/bootstrap.md) |
