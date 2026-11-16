# AI Providers

The agent talks OpenAI-compatible chat completions — the de-facto
standard — so any compatible gateway works. Three presets ship and a
custom gateway can be added in minutes.

## Built-in presets

| Preset | base_url | Default model | Key variable |
|---|---|---|---|
| `kilo` (default) | `https://api.kilo.ai/api/gateway` | `kilo-auto/free` | `KILO_API_KEY` |
| `opencode` (OpenCode Zen) | `https://opencode.ai/zen/v1` | `big-pickle` | `OPENCODE_API_KEY` |
| `openrouter` | `https://openrouter.ai/api/v1` | `openrouter/auto` | `OPENROUTER_API_KEY` |

Switch with `/provider` inside the agent, or by editing
`~/.noxs/ai/config.json` — see [Configuration](configuration.md).

## Custom gateways

Any endpoint implementing

```
POST {base_url}/chat/completions
{"model": …, "messages": […], "tools": […], "stream": bool}
```

works: set `provider`/`base_url`/`model`/`api_key_env` in the config
(or the `NOXS_AI_*` environment variables). Tool calling follows the
OpenAI tool-call schema; streaming is SSE with `data:` chunks and a
`[DONE]` terminator.

## Request behavior

- Streaming and non-streaming modes.
- Bounded exponential backoff — default 3 retries, delays capped.
- HTTP 429 honors `Retry-After`.
- 401/403 map to an auth error with a clear user hint.
- Cooperative cancellation (Ctrl+C) aborts in-flight requests and
  tool batches.

## What the provider never sees

- Your provider key (it stays in the named environment variable — see
  [API keys](api-keys.md)).
- Secrets from tool output: results are secret-redacted before they
  reach the model.
- Unrestricted environment variables: the system prompt exposes only
  safe environment facts (arch, OS, cwd, tool list).

## Availability

Provider choice does not change tool behavior or permission gates —
the same Tool Registry and `Allow? [y/N]` flow apply regardless of
gateway. If a gateway is down the agent reports the mapped error
(`unavailable`, `rate_limit`, `timeout`, `auth`, `malformed`) — see
[Troubleshooting](troubleshooting.md).
