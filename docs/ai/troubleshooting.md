# AI Troubleshooting

## Start here

```console
noxs@ubuntu:~$ nx ai --help
noxs@ubuntu:~$ nx ai "say hello"
```

Inside the agent, `/status` shows the live configuration and `/tools`
lists the registered tools.

## Provider errors and fixes

The provider client maps failures to deterministic codes
(`AIProviderError`):

| Code | Meaning | Fix |
|---|---|---|
| `timeout` | Request/stream timed out (90 s default) | Retry; check `noxs network status`; large prompts take longer |
| `rate_limit` | HTTP 429 from the gateway | Wait — `Retry-After` is honored automatically |
| `unavailable` | 5xx or unreachable gateway | Retry; check the provider's status page |
| `auth` | 401/403 — credentials rejected | Check the key variable is set and valid — see [API keys](api-keys.md) |
| `malformed` | Unexpected response shape | Usually a non-OpenAI-compatible endpoint — check `base_url` |
| `cancelled` | You cancelled (Ctrl+C) | Nothing to fix |

Retries are bounded (default 3) with exponential backoff; nothing
retries forever.

## Common situations

**`Noxs AI runtime is not installed (missing /usr/local/lib/noxs/ai/agent.py)`**
— the AI runtime files are not in this environment. Re-run the app's
setup/repair, or reinstall the environment.

**`Could not install python3. Install it manually: sudo apt install python3`**
— the auto-install failed (network or apt state). Install python3 by
hand and re-run `nx ai`.

**Auth errors right after changing providers** — the key variable name
changes with the preset (`KILO_API_KEY` vs `OPENCODE_API_KEY` vs
`OPENROUTER_API_KEY`); export the matching one.

**Streaming works but output is empty** — some gateways send
keepalives only; try `--no-stream` to isolate.

**Agent hits `MAX_AGENT_STEPS`** — the task loop reached the step cap
(30 by default). Raise the limit in `~/.noxs/ai/config.json` or split
the task.

**Key appears in a log?** It should not — logging excludes keys,
passwords and file contents by design (`~/.noxs/ai/agent.log` records
session, tool, duration, outcome). If you ever see otherwise, report it
at <https://github.com/crossberry-in/noxs/issues>.
