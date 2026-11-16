# Command Execution

Every terminal command runs inside the environment's bash under proot.
This page explains the execution model, the two CLI entry points and
how permissions fit in.

## Execution model

```
Android app (your keystrokes)
   └─ native PTY (forkpty, JNI bridge)
        └─ proot (fake root -0, path virtualization)
             └─ /bin/su -s /bin/bash -l noxs   →  your command
```

- A **real PTY** carries input/output; resize, Ctrl-C, job control and
  full-screen programs behave like on a real computer.
- proot virtualizes paths via ptrace: the guest sees `/`, `/home`,
  `/var/run/noxs/…` — all resolved inside app-private storage.
- `sudo` works normally inside the sandbox (password-protected) and
  controls the environment only.

## Two CLIs, one command space

| CLI | Role |
|---|---|
| `noxs` | The core environment CLI: `status`, `update`, `info`, `ubuntu status`, `code`, `docker`, `storage`, plus every Android-bridge command |
| `nx` | The package + extensions CLI (`nx pkg`, `nx install`, `nx ai`, `nx plug`, `nx vpn`, `nx cert-fix`, `nx ow`, …) **and a forwarder**: any unknown command is executed as `noxs <cmd>` |

So `nx docker install`, `nx storage status`, `nx files` and
`nx sms contacts` are all valid — they forward to the matching `noxs`
command. See [nx command system](../cli/nx.md) and
[noxs CLI reference](../cli/noxs.md).

## Exit codes and errors

- Noxs CLI commands print `noxs: <message>`; errors go to stderr with a
  non-zero exit code.
- Unknown commands respond with `noxs: unknown command: <cmd> (try:
  noxs help)` and exit 2.
- Package operations use stable error codes such as
  `PACKAGE_NOT_FOUND`, `CHECKSUM_MISMATCH`, `NETWORK_ERROR` — the full
  table lives in [Error codes](../reference/error-codes.md).

## Long-running setup operations

Bootstrap and repair operations print live status lines with a spinner
and a monotonic elapsed clock, end with `✓ <name> <elapsed>` (or `✗`),
and never fake progress percentages — see
[Terminal interface](terminal-interface.md#setup-live-long-running-operations).

## Safe use

Commands typed in the terminal run with the sandbox's rights, which
means they can modify everything inside the environment — including
deleting your files. Destructive commands are ordinary Linux commands;
Noxs adds no safety net around `rm -rf`. Android-side effects (storage,
SMS, camera, notifications) always go through the explicit bridge
commands listed in [Android Integration](../android/overview.md).
