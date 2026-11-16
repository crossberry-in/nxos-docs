# Error Codes

Verified error identifiers across the Noxs CLIs. Codes are stable;
user-facing messages may vary.

## NX Package System

Stable uppercase codes (CLI messages + `--json` output):

| Code | Raised when |
|---|---|
| `PACKAGE_NOT_FOUND` | No package/version in any source |
| `UNSUPPORTED_ARCHITECTURE` | No asset for this device architecture |
| `NETWORK_ERROR` | Sources unreachable |
| `DOWNLOAD_FAILED` | Transfer failed (second attempt resumes) |
| `CHECKSUM_MISMATCH` | sha256 differs from registry/sidecar |
| `SIGNATURE_VERIFICATION_FAILED` | apt signature verification failed |
| `DEPENDENCY_RESOLUTION_FAILED` | apt dependency resolution failed |
| `INSUFFICIENT_DISK_SPACE` | Not enough free space for the operation |
| `INSTALL_PERMISSION_DENIED` | Installation blocked |
| `PACKAGE_MANAGER_BUSY` | Another package operation holds the single-flight lock |
| `MIRROR_UNAVAILABLE` | Mirror unreachable while required (`NOXS_PKG_REQUIRE_MIRROR=1`) |

Fixes per code: [Package troubleshooting](../packages/package-troubleshooting.md).

## AI provider client

Lowercase codes from `AIProviderError`:

| Code | Raised when |
|---|---|
| `timeout` | Request/stream exceeded the timeout |
| `rate_limit` | HTTP 429 (honors `Retry-After`) |
| `unavailable` | 5xx or unreachable gateway |
| `auth` | 401/403 — credentials rejected |
| `malformed` | Unexpected response shape |
| `cancelled` | Cooperative cancellation (Ctrl+C) |

Retry behavior: bounded exponential backoff (default 3 retries) for
`unavailable`, `rate_limit`, `timeout` only. See
[AI troubleshooting](../ai/troubleshooting.md).

## CLI exit codes

| Exit | Meaning |
|---|---|
| 0 | Success |
| 1 | Operation failed (message on stderr) |
| 2 | Usage error — unknown command or missing arguments |

Bridge operations surface `ERR\n<message>` over the request/response
transport; the CLI prints the message and exits non-zero — see
[Android integration](../android/overview.md#architecture).
