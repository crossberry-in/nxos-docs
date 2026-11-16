---
name: api-reference
description: API reference pages
---

# nxos-docs skill: api-reference

purpose: Maintain reference/sdk-reference.md, error-codes.md and manifest references.
when_to_use: Bridge operations, SDK, manifests, error codes change.
required_context: Bridge ops are defined in NoxsAndroidBridge.kt execute() + uiOperations; error codes in the pkg system.
relevant_files:
  - docs/reference/sdk-reference.md
  - docs/reference/error-codes.md
  - docs/reference/package-manifest.md
  - docs/reference/plugin-manifest-reference.md
workflow:
  1. Only document operations that exist in source; mark experimental ones.
  2. Keep request/response format examples exact (OK/ERR line + text).
coding_rules: Field tables complete; no invented fields.
security: Never document internal endpoints holding credentials.
testing: strict build.
documentation_updates: the task itself.
checklist:
  - operations match source
  - formats exact
