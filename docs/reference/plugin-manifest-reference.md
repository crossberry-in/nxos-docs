# Plugin Manifest Reference

The canonical `plugin.json` schema — field table, validation rules and
the SDK requirement fields — lives in the Plugin SDK section:

**[Plugin Manifest Reference (plugin.json)](../plugins/plugin-manifest.md)**

Quick summary:

| Field group | Fields |
|---|---|
| Identity | `id`, `name`, `version`, `description`, `main` |
| Access | `permissions`, `minimumNoxsVersion` |
| Presentation | `logo`, `readme`, `author`, `license`, `category`, `keywords`, `homepage`, `repository`, `commands` |
| SDK contract | `sdkVersion`, `minimumSdkVersion`, `maximumSdkVersion`, `apiFeatures` (`logging`, `ui`, `terminal`, `storage`) |

Related references:

- [SDK releases and features](../plugins/plugin-sdk.md#capability-table)
- [Plugin lifecycle](../plugins/plugin-lifecycle.md)
- [Permission catalog](../android/app-permissions.md#permission-catalog)
