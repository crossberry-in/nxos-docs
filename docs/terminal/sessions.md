# Sessions

A session is one running shell (plus its processes) attached to a
terminal tab. Noxs supports multiple simultaneous sessions, each bound
to the active environment.

## Managing sessions

- Open multiple sessions from the terminal's session tabs.
- The header shows a subtle status line per session:
  `● RUNNING <label> · PID <n>` (output within the last 10 s),
  `○ IDLE`, `✓ EXITED (code)`, `✗ FAILED (code)`.
- The editor (code-server) follows your session's working directory via
  OSC 7 — see [Directory navigation](../files/directory-navigation.md).

## Background behavior

Terminal settings include **Keep sessions alive in background** and
**Restore previous sessions** (see
[Customization](customization.md#behavior)). When keep-alive is on,
sessions survive app switches; a foreground-service notification is
used for long-running operations when notifications are permitted —
see [Background execution](../android/background-execution.md).

## Scrollback per session

Each session has its own bounded ring-buffer scrollback (default
10,000 lines, configurable 1,000–50,000). Clearing scrollback never
touches the screen, shell history, the filesystem or running processes.

## Ending sessions

- Closing a tab ends that session's shell; other sessions are
  unaffected.
- The shell's ordinary exit (`exit`, Ctrl-D) ends the session and the
  status line reports the exit code.
- `--kill-on-exit` is applied to proot, so nothing leaks after the app
  process goes away.

## Working directory and environment

New sessions start in `/home/noxs` with the standard login environment
(see [Shell configuration](shell-configuration.md)). Sessions are never
restarted by UI toggles such as full screen — the shell keeps running.
