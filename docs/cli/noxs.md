# The `noxs` CLI

`noxs` is the core environment CLI inside the Linux terminal. It lives
at `/usr/local/bin/noxs` and owns the environment lifecycle plus every
guest→Android bridge command. The `nx` hub forwards to it, so `nx
storage status` == `noxs storage status`.

```
noxs help                             command list
noxs status                           environment health summary
noxs update                           apt metadata refresh + upgrade
noxs info                             session/account/storage facts
noxs ubuntu status                    Ubuntu identity + repository report
noxs code install|start|stop|restart|status|logs
noxs docker install|start|stop|restart|status|info|test
noxs storage status|setup|map|repair|reset|ls|mkdir|cat|get|put|rm|cp|mv|
                     permission|grant|revoke|mount|unmount|list
noxs files                            open the Noxs file browser (Android UI)
noxs document open|import|export|gallery|picker
noxs sms status|permission|send|compose|contacts
noxs device info|battery|storage
noxs notification status|permission|post <title> [body...]
noxs share <file> | noxs share -t <text>
noxs camera [dest]
noxs clipboard get|set <text>
noxs network status
noxs-service start|stop|restart|status [service]
noxs-socket list|test <path>
noxs-ps
```

## Environment commands

- `noxs status` — health summary (sources, certificates, apt state,
  session label); rows print `OK`/`WARN` with a repair hint.
- `noxs ubuntu status` — pretty name, version, codename, kernel (host
  kernel via proot), architecture, shell, apt host, keyring, package
  index.
- `noxs update` — native apt update + non-interactive upgrade.
- `noxs info` — session, account and storage facts.

## code-server

`noxs code …` manages the built-in editor server — local-only by
design (binds `127.0.0.1`, random password, mode 600 config). Full
reference: [Code Server](../devtools/code-server.md).

## Docker

`noxs docker …` installs and controls Docker inside the environment
(`docker.io` from Ubuntu repos). Honest capability model — see
[Docker support](docker.md).

## Storage

`noxs storage …` — SAF folder access, the opt-in `/sdcard` direct
mount and the permission dashboard. Full reference:
[Storage commands](../android/storage-permissions.md).

## Android bridge commands

| Command | Effect |
|---|---|
| `noxs files` | Opens the Noxs file browser (Android UI) |
| `noxs document open|import|export|gallery|picker` | SAF/Photo-Picker file flows — [File picker](../android/file-picker.md) |
| `noxs sms status|permission|send|compose|contacts` | SMS through **your own SMS app** — no SMS permission is requested or held. See [Permissions](../android/app-permissions.md) |
| `noxs device info|battery|storage` | Non-identifying device reports |
| `noxs notification status|permission|post` | Post a user-authorized notification |
| `noxs share <file>` / `noxs share -t <text>` | Android Sharesheet |
| `noxs camera [dest]` | Native camera app; capture handed back as a file |
| `noxs clipboard get|set <text>` | Android clipboard (foreground-only) |
| `noxs network status` | Transport/metered/validation summary — no identifiers |

Every operation is optional and user-authorized through Android's own
permission UI — see [NX Android Integration](../android/overview.md).

## Services and sockets

- `noxs-service start|stop|restart|status [service]` — manage guest
  services; `noxs-ps` lists environment processes.
- `noxs-socket list|test <path>` — verify Unix socket paths (the
  `/var/run/noxs/…` tree) — see
  [Unix domain sockets](../architecture/unix-sockets.md).
