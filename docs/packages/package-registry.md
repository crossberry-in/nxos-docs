# Package Registry

Every NX package describes its releases in a `registry.json` at the
repository root. Noxs reads this file — as data, never executed — to
resolve, verify and install releases. Three registry surfaces exist.

## 1. The package repository registry.json

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

- Maintained by the release workflow — you never edit release metadata
  by hand.
- `versions` preserves history; `latest` is the install default.
- Asset names follow `<name>.nx.pkg.<version>.<arch>.tar.xz` (+ a
  `.sha256` sidecar).

## 2. NXMirror Cloud

Sign in once, then publish from the package directory:

```console
noxs@ubuntu:~$ nxc register     # create account (first time)
noxs@ubuntu:~$ nxc login        # later logins
noxs@ubuntu:~$ nxc whoami       # verify the account
noxs@ubuntu:~$ nx pkg deploy    # build + upload the current package
noxs@ubuntu:~$ nxc packages     # list your cloud packages
noxs@ubuntu:~$ nxc logout
```

- The artifact is uploaded to the account's storage, **not** committed
  into the Noxs source repository; versions are immutable and store
  artifact URL, byte size and SHA-256.
- Direct CLI uploads are limited to **4 MiB per artifact** by the
  Netlify request limit — larger packages publish through GitHub
  Releases.
- `nx git` opens the Git Cloud web interface
  (`https://nxmirror.netlify.app/`).

## 3. Official packages (noxs-pkg organization)

The sources of the official packages live in the `nx-pkg/` directory of
the noxs repository; each is published as its own public Git repository
under `github.com/noxs-pkg/<name>`:

| package | language | what it does |
|---|---|---|
| `tree` | C++ | directory tree printer |
| `nxinfo` | Node.js | Noxs environment info |
| `nxfetch` | Python | compact system summary |

`nx install tree` resolves, verifies and installs straight from that
repository's releases.

## Resolution order

`nx pkg search` / `nx pkg info` merge several sources with a defined
priority: local cache → Noxs package API → distro metadata → registry
— see the [package manager overview](package-manager.md#distro-packages-nx-pkg-debian-ubuntu).
