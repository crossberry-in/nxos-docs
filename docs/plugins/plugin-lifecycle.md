# Plugin Lifecycle

Plugins are installed under `~/.noxs/plugins/<id>/` in the active
environment and managed from the Plugins screen (Noxs sidebar →
Plugins) or the `nx plug` CLI.

## States and transitions

```
             install                 enable
  ┌───► INSTALLED ───► ENABLED ───┐
  │        │  ▲            │      │
  │ update │  └─ disable ──┘      │
  │        ▼                      │
  └──── revisits store      uninstall
```

| Operation | UI | CLI |
|---|---|---|
| Browse/search | Plugin Store | `nx plug search <query>` |
| Install | Store details page | `nx plug install <id>` |
| Enable / disable | Plugins list toggle | `nx plug enable|disable <id>` |
| Update | Store (when a new version exists) | `nx plug update <id>` |
| Uninstall | Plugins list | `nx plug uninstall <id>` |
| Metadata | Details page | `nx plug info <id>` |

## What install does

1. The artifact is downloaded over HTTPS (registry-published release),
2. SHA-256 verified against the registry checksum,
3. member-checked and extracted with the same safe tar handling as NX
   packages,
4. the extracted `plugin.json` is re-validated (id must match the
   registry),
5. files land at `~/.noxs/plugins/<id>/` and any `bin` commands are
   recorded in the plugin's `.bin-manifest` so uninstall removes
   exactly what install added.

## Runtime

- `NoxsPluginManager` resolves the plugin's SDK requirements and loads
  `main` (normally `plugin.js`) with the resolved SDK — see
  [Plugin SDK](plugin-sdk.md#runtime-flow).
- Disabled plugins stay on disk but are not loaded.
- Per-plugin state (SDK version, digests) lives in `plugin-state.json`;
  plugin-scoped KV storage (SDK `storage` feature) in
  `.storage.json`.

## Update and uninstall

- Updates fetch the new release, verify, and replace the plugin
  directory contents; published versions are immutable.
- Uninstall removes the directory **plus** the commands recorded in
  `.bin-manifest` — nothing else is touched.
- Removing an environment removes its plugins with it (they live in
  that rootfs's home).

## Permissions at runtime

Permissions declared in
[`plugin.json`](plugin-manifest.md#fields) are validated against the
Permission Center on every privileged API request — grants are never
automatic and always visible; see
[App permissions](../android/app-permissions.md).
