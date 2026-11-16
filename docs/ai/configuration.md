# AI Configuration

`nx ai` is configured through one JSON file plus environment-variable
overrides. Provider, endpoint, model and key variable are all
configuration — replaceable without touching the agent.

## Config file

`~/.noxs/ai/config.json` (or `--config <path>`):

```json
{
  "enabled": true,
  "provider": "kilo",
  "model": "kilo-auto/free",
  "stream": true,
  "max_steps": 30,
  "max_tool_calls": 50,
  "max_parallel_tools": 4
}
```

| Key | Default | Meaning |
|---|---|---|
| `enabled` | `true` | Agent availability |
| `provider` | `kilo` | Active provider preset — see [Providers](providers.md) |
| `model` | `kilo-auto/free` | Model id sent to the gateway |
| `base_url` | preset value | Gateway root (OpenAI-compatible chat completions) |
| `api_key_env` | preset value | Environment variable holding the key |
| `stream` | `true` | SSE streaming responses |
| `max_steps` / `max_tool_calls` / `max_parallel_tools` | 30 / 50 / 4 | Agent loop limits (clamped, ≥ 1) |
| `max_tool_output` | ~12k chars (min 1000) | Per-tool output cap |
| `request_timeout_sec` | 90 | HTTP timeout |
| `max_retries` | 3 | Bounded exponential backoff |
| `max_runtime_sec` | 900 | Whole-session runtime cap |
| `full_session` | `true` | Session history handling |

## Environment overrides

| Variable | Sets |
|---|---|
| `NOXS_AI_PROVIDER` | active provider |
| `NOXS_AI_MODEL` | model |
| `NOXS_AI_BASE_URL` | gateway endpoint |
| `NOXS_AI_API_KEY_ENV` | which env var holds the API key |
| `NOXS_AI_API_KEY` | fallback key variable read by the client |

## CLI flags

```console
noxs@ubuntu:~$ nx ai --help
    --model <model>    override the configured model (default: kilo-auto/free)
    --no-stream        disable streaming responses
    --yes              auto-approve CONFIRM-level tools (one-shot only)
    --config <path>    use an alternative config file
```

## In-agent commands

`/provider` manages AI gateways interactively (Kilo, OpenCode Zen,
OpenRouter, custom); `/model` shows or switches the model; `/status`
and `/config` report the live configuration. The full command list is
in the [agent overview](nx-ai.md#agent-commands-spec-23).

## Precedence

CLI flags > environment variables > provider store (`/provider`
selection) > `config.json` > built-in defaults.
