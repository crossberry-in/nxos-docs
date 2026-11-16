# Package Manifest Reference

The package manifest is `registry.json` at a package repository root.
Noxs parses it strictly as data (never shell or code) and validates
every field before use in URLs or paths. Field reference; the publishing
flow lives in [Package registry](../packages/package-registry.md).

## Schema

```json
{
  "name": "tree",
  "description": "Noxs tree utility",
  "latest": "1.0.1",
  "versions": [
    {
      "version": "1.0.0",
      "tag": "tree-v1.0.0",
      "files": [
        {
          "name": "tree.nx.pkg.1.0.0.aarch64.tar.xz",
          "sha256": "…"
        }
      ]
    }
  ]
}
```

## Fields

| Field | Type | Meaning |
|---|---|---|
| `name` | string | Package identifier, used in asset names and paths (strictly validated) |
| `description` | string | Free text shown by `nx pkg info` |
| `latest` | string | Install default; the workflow bumps it on release |
| `versions` | list | Release history, sorted by version |
| `versions[].version` | string | Semantic version |
| `versions[].tag` | string | Release tag (`<name>-v<version>`) |
| `versions[].files` | list | Published assets |
| `files[].name` | string | Asset file name (`<name>.nx.pkg.<version>.<arch>.tar.xz`) |
| `files[].sha256` | string | Asset digest, re-verified at install time |

## Rules enforced by the installer

- The requested version must exist in `versions`, otherwise
  `PACKAGE_NOT_FOUND`.
- An asset matching the device architecture (`aarch64`, `x86_64`,
  `armv7`) is selected; a `universal` asset covers
  architecture-independent packages, otherwise
  `UNSUPPORTED_ARCHITECTURE`.
- The downloaded artifact's SHA-256 must match **both** the `sha256`
  here and the published `.sha256` sidecar, else `CHECKSUM_MISMATCH`.
- Names, versions, repository ids and asset names are validated before
  they are used in URLs or paths; registry fields are never evaluated
  as shell code.

## Maintenance

`registry.json` is maintained automatically by the package release
workflow (versions preserved, `latest` bumped, committed with
`[skip ci]`) — you never edit release metadata by hand.
