# CLI Reference

Every command below is verified against the shipped CLI scripts
(`nx`, `noxs`, `nxc`, `noxs-service`, `noxs-socket`, `noxs-ps`).
Detailed pages are linked; this page is the quick table.

## nx — package system and extensions

| Command | Purpose |
|---|---|
| `nx pkg init <name> [--node|--rust|--cpp|--python|--go]` | Scaffold a package project |
| `nx pkg build` | Build the current package |
| `nx pkg release` | Pre-flight release validation |
| `nx pkg deploy` | Build + publish to NXMirror Cloud |
| `nx pkg info <name>` | Merged view: mirror + distro + registry + installed |
| `nx pkg search <name> [--json]` | Search cache → Noxs API → distro → registry |
| `nx pkg install <name> [-y] [--json]` | Install via apt or the NX installer |
| `nx pkg update [--full]` | Refresh indexes; `--full` runs the upgrade |
| `nx pkg list` | Installed packages (Ubuntu + Noxs) |
| `nx pkg remove <name> [-y]` | Remove via apt or the package manifest |
| `nx pkg doctor` | Package-layer health check |
| `nx install <pkg>[@version]` | Install an official package |
| `nx install -git @user/repo[@version]` | Install from any GitHub registry |
| `nx list` / `nx info <pkg>` / `nx update [pkg]` / `nx remove <pkg>` | Installed-package management |
| `nx ow <url>` | Open a URL in the Noxs browser window |
| `nx vpn` / `stop` / `status` / `test` / `on` / `off` | Tor over PRoot |
| `nx plug` / `search` / `list` / `info` / `install` / `update` / `uninstall` / `enable` / `disable` | Plugin Store |
| `nx ai [task]` | AI Agent Terminal (`--model --no-stream --yes --config`) |
| `nx cert-fix` | APT + CA certificate repair |
| `nx git` | Open NXMirror Git Cloud |
| `nx whoami` | Show the signed-in NXMirror account |
| `nx nxc …` | Call the NXMirror CLI directly |
| `nx version` | Print the CLI version |
| `nx <anything-else>` | Forwarded verbatim to `noxs` |

## noxs — environment core

| Command | Purpose |
|---|---|
| `noxs help` | Command list |
| `noxs status` | Environment health summary |
| `noxs update` | apt metadata refresh + upgrade |
| `noxs info` | Session/account/storage facts |
| `noxs ubuntu status` | Ubuntu identity + repository report |
| `noxs code install|start|stop|restart|status [--json]|logs` | code-server lifecycle |
| `noxs docker install|start|stop|restart|status|info|test` | Docker lifecycle |
| `noxs storage <command>` | SAF + mount commands — see [storage reference](../android/storage-permissions.md) |
| `noxs files` | Open the Noxs file browser (Android UI) |
| `noxs document open|import|export|gallery|picker` | Android document flows |
| `noxs sms status|permission|send|compose|contacts` | SMS via your own SMS app |
| `noxs device info|battery|storage` | Non-identifying device reports |
| `noxs notification status|permission|post <title> [body...]` | Notifications |
| `noxs share <file>` / `noxs share -t <text>` | Android Sharesheet |
| `noxs camera [dest]` | Camera capture to a file |
| `noxs clipboard get|set <text>` | Clipboard |
| `noxs network status` | Transport/metered/validation summary |

## NXMirror Cloud — `nxc`

| Command | Purpose |
|---|---|
| `nxc register` / `nxc login` / `nxc logout` | Account management |
| `nxc whoami` | Verify the signed-in account |
| `nxc packages` | List your cloud packages |
| `nxc pkg deploy <dir>` | Publish a package directory |

## Helpers

| Command | Purpose |
|---|---|
| `noxs-service start|stop|restart|status [service]` | Guest service management |
| `noxs-socket list` / `noxs-socket test <path>` | Unix socket checks |
| `noxs-ps` | List environment processes |

## Conventions

- Errors print as `noxs: <message>` (stderr) with non-zero exit.
- Unknown commands: `noxs: unknown command: <cmd> (try: noxs help)`.
- Package operations use stable error codes — see
  [Error codes](error-codes.md).
- `nx` == `noxs` for every `noxs` command (transparent forwarder).
