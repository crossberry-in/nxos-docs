# Plugin Manifest Reference (plugin.json)

Every plugin carries a `plugin.json`. The app parses it as data —
never executed — and validates it at download, install and load time.
This page is the field reference; the authoring flow lives in
[Plugin SDK](plugin-sdk.md).

## Full schema

```json
{
  "id": "my-plugin",
  "name": "My Plugin",
  "version": "1.2.0",
  "description": "What the plugin does",
  "main": "plugin.js",
  "permissions": ["notifications.show"],
  "minimumNoxsVersion": "1.3.0",
  "logo": "icon.svg",
  "readme": "README.md",
  "author": "Your Name",
  "license": "MIT",
  "category": "utilities",
  "commands": ["mytool"],
  "keywords": ["tools", "example"],
  "homepage": "https://example.com/my-plugin",
  "repository": "https://github.com/you/my-plugin",
  "sdkVersion": "0.0.2",
  "minimumSdkVersion": "0.0.1",
  "maximumSdkVersion": null,
  "apiFeatures": ["storage"]
}
```

## Fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | `[a-z0-9][a-z0-9-]{1,63}` — must match the registry entry |
| `name` | string | yes | Display name |
| `version` | string | yes | Semantic version (parsed; invalid versions fail validation) |
| `description` | string | yes | One-line summary |
| `main` | string | yes | Runtime entry, normally `plugin.js` |
| `permissions` | string[] | no | Noxs permission ids from the [catalog](../android/app-permissions.md#permission-catalog) |
| `minimumNoxsVersion` | string | no | Defaults to `0.0.0` |
| `logo` | string | no | Icon file in the plugin directory |
| `readme` | string | no | Defaults to `README.md` |
| `author`, `license`, `category` | string | no | Metadata for the store details page |
| `commands` | string[] | no | Guest CLI commands the plugin installs into `bin` |
| `keywords` | string[] | no | Store search terms (search covers id, name, category, keywords, description) |
| `homepage`, `repository` | string | no | Links shown on the details page |
| `sdkVersion` | string | no | Defaults to `0.0.1` — the exact API generation legacy plugins were built on |
| `minimumSdkVersion` / `maximumSdkVersion` | string | no | Accepted SDK range (inclusive) |
| `apiFeatures` | string[] | no | Required SDK features — one of `logging`, `ui`, `terminal`, `storage`; unknown features fail validation |

## Validation rules

- Broken JSON → the manifest is rejected ("plugin.json unreadable" /
  "Invalid JSON: …").
- The staged install tree must carry a valid `plugin.json` whose `id`
  matches the registry record.
- `apiFeatures` entries are validated against the SDK contract's
  feature list; unknown features are rejected with a clear problem
  message.
- SDK resolution (`PluginSdkCatalog.resolve`) requires: same API
  generation, an inclusive `[minimumSdkVersion, maximumSdkVersion]`
  match, full feature coverage, and picks the newest installed
  compatible SDK first.

## Registry side

The Plugin Store's `registry.json` mirrors most of these fields per
entry (plus `artifact`, `checksum`, `releaseTag`, `updatedAt`) — see
the [Plugin Store flow](plugin-sdk.md#store-integration).
