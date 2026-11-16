# AI API Keys and Security

## How keys are handled

- The API key is read **only** from the environment variable named by
  configuration (`api_key_env`), with `NOXS_AI_API_KEY` as the fallback
  name.
- The key is **never** logged, printed, or included in error messages.
- No provider keys are embedded anywhere in Noxs — the app-side tests
  (`NoxsNxAiTest`) verify that no keys ship in the binary or templates.
- The agent runtime execs with a minimal, clean environment; tool
  subprocesses get a restricted environment and never inherit secrets.

## Providing a key

```console
noxs@ubuntu:~$ export KILO_API_KEY="sk-…"        # default preset
noxs@ubuntu:~$ nx ai
```

For other presets use the matching variable (`OPENCODE_API_KEY`,
`OPENROUTER_API_KEY`) or point `api_key_env` at your own — see
[Providers](providers.md).

Keys set with `export` live for the session. To persist one, put the
export in your own `~/.bashrc` — at your own risk; the file is part of
your home and is covered by the sandbox's normal file permissions.

!!! danger "Never commit or share keys"
    Do not paste keys into screenshots, issue reports, plugin code or
    the docs. If a key leaks, revoke it at the provider immediately.

## Protected paths and secret filtering

The agent's tool layer denies operations outside the Noxs filesystem
scope and protects credential paths (`~/.ssh/`, `.gnupg/`, `.aws/`,
`/etc/shadow`, …). Tool results are secret-redacted before reaching
the model, and `terminal.run` commands pass a validator (destructive
blocklist, length cap) before execution.

## The permission gate

CONFIRM-level tools always ask — and the confirmation is controlled by
Noxs, never simulated by the model:

```
⚠ Action requires permission
Tool: file.delete
Target: 24 files
Allow? [y/N]
```

One-shot mode can pre-approve CONFIRM tools with `--yes` — you asked
for the task, but the tool list stays visible in the transcript.

## Related security pages

- [Security model](../architecture/security.md) — the overall threat
  model and the proot isolation caveat.
- [Permission Center](../android/app-permissions.md) — Android-side
  permission gating.
- [Plugin permissions](../plugins/plugin-sdk.md) — the SDK permission
  boundaries.
