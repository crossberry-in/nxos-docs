# SDK Reference

Noxs exposes two SDK surfaces behind the Permission Center. This page
is the entry point; each link goes to the full reference.

## @noxs/nx-api — the package SDK

The SDK used by NX packages (installed via the NX Package System) to
request capabilities from the host app.

- Overview, install and usage: [`@noxs/nx-api`](../plugins/nx-api.md)
- Permission ids and gating: [Permission catalog](../android/app-permissions.md#permission-catalog)
- Privileged requests are validated on every call; denied
  permissions surface as errors, never silent no-ops.

## Noxs Plugin SDK — the plugin SDK

The versioned JavaScript API plugins run against, with a pinned
compatibility matrix.

| SDK | apiVersion | Features | Minimum Noxs |
|---|---|---|---|
| 0.0.1 | 1 | logging, ui, terminal | 0.11.0 |
| 0.0.2 | 1 | logging, ui, terminal, storage | 0.13.0 |

- Capability table and runtime flow:
  [Plugin SDK](../plugins/plugin-sdk.md#capability-table)
- Manifest fields (`sdkVersion`, `apiFeatures`, …):
  [Plugin manifest reference](../plugins/plugin-manifest.md)
- Ecosystem-side docs (publishing, examples): the
  [noxs-plugins repository](https://github.com/web12-app/noxs-plugins),
  `docs/SDK.md`

## Error surfaces

| Surface | Errors | Reference |
|---|---|---|
| NX package CLI | stable uppercase codes (`PACKAGE_NOT_FOUND`, `CHECKSUM_MISMATCH`, …) | [Error codes](error-codes.md) |
| AI provider client | lowercase codes (`timeout`, `rate_limit`, `unavailable`, `auth`, `malformed`, `cancelled`) | [AI troubleshooting](../ai/troubleshooting.md) |
| Android bridge | `ERR\n<message>` responses over the request/response transport | [Android integration](../android/overview.md#architecture) |

## Stability promises

- SDK releases are additive and pinned: a plugin gets exactly the API
  generation it was built on — the default never introduces a newer
  API than the plugin has seen.
- CLI error codes are stable identifiers; messages may improve, codes
  do not change meaning.
- The Android bridge transport is internal; plugins and packages go
  through the SDKs, not the raw bridge.
