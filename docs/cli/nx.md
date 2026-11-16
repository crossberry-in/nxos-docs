# The `nx` Command System

`nx` is Noxs's command hub inside the Linux terminal: the NX package
system, the AI agent, the Plugin Store, web/VPN helpers — and a
transparent forwarder for every `noxs` command.

```
nx pkg init <name> [--node|--rust|--cpp|--python|--go]
nx pkg build | release | deploy | info | search | install | update | list | remove | doctor
nx install <pkg>[@version] | nx install -git @user/repo[@version]
nx list | info <pkg> | update [pkg] | remove <pkg>
nx ow <url>            open a URL in the Noxs floating browser window
nx vpn <cmd>           Tor over PRoot (VPN mode)
nx plug <cmd>          Noxs Plugin Store
nx ai [task]           Noxs AI Agent Terminal
nx cert-fix            repair APT sources, CA certificates, curl/wget
nx git                 open NXMirror Git Cloud
nx whoami              show the signed-in NXMirror account
nx help                full usage
```

`nx` also forwards anything else to the `noxs` CLI — `nx docker install`,
`nx code start`, `nx storage status`, `nx files`, `nx sms contacts` all
work (see the [noxs CLI](noxs.md)).

## Setup

!!! note "There is no `nx setup` command"
    Environment setup happens through the app's setup flow
    ([Initial setup](../getting-started/initial-setup.md)), not a CLI
    command. Typing `nx setup` falls through the forwarder to `noxs`,
    which reports `unknown command`. In-terminal maintenance commands
    that *do* exist: [`nx cert-fix`](cert-fix.md), `noxs status`,
    `nx pkg doctor`.

## Package commands

- **Users**: `nx install tree`, `nx install tree@1.0.0`,
  `nx install -git @web12-app/tree`, `nx list`, `nx info tree`,
  `nx update`, `nx remove tree`.
- **Authors**: `nx pkg init` scaffolds a language template with
  GitHub Actions release automation; `nx pkg build` / `nx pkg release`
  build and pre-flight locally; `nx pkg deploy` publishes to NXMirror
  Cloud.
- Full flows and the registry format live in
  [NX Package System](../packages/package-manager.md).

## Web and VPN

- `nx ow <url>` — opens the URL in the Noxs native browser window
  (real `android.webkit.WebView` in a floating window). See
  [Native browser](web-browser.md).
- `nx vpn` — Tor over PRoot: `nx vpn` (install+activate), `stop`,
  `status`, `test`, `on|off` (route new shells globally).

## Plugin Store

`nx plug` opens the store UI; `search`, `list`, `info`, `install`,
`update`, `uninstall`, `enable`, `disable` manage plugins from the
terminal. See [Plugin SDK](../plugins/plugin-sdk.md).

## AI

`nx ai` starts the agent REPL (`nx@ai>`); `nx ai "task"` runs one shot.
Options: `--model`, `--no-stream`, `--yes` (one-shot only),
`--config <path>`. See [NX AI](../ai/nx-ai.md).

## Maintenance

- [`nx cert-fix`](cert-fix.md) — APT sources + CA certificate repair,
  curl/wget provisioning. Also repairs legacy Debian guests.
- `nx whoami` / `nx git` / `nxc` — NXMirror Cloud account and Git
  interface (`https://nxmirror.netlify.app/`).

## Version

`nx version` / `nx --version` prints the CLI version.
