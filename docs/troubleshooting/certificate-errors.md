# Certificate Errors

Full repair guide: [`nx cert-fix`](../cli/cert-fix.md). This page is
the symptom index.

## Symptoms

| Symptom | Cause |
|---|---|
| `E: Unable to locate package curl` | Empty package lists — bootstrap never completed |
| `Certificate verification failed` / TLS handshake errors in apt or curl/wget | Missing/stale CA bundle |
| `GPG error … NO_PUBKEY` | Missing keyring (`ubuntu-keyring`) |
| `E: The repository … is not signed` | Broken or missing `noxs.sources` |
| `curl: (60) SSL certificate problem` | CA bundle absent — curl/wget are not even installed on a fresh minimal rootfs |

## One-command repair

```console
noxs@ubuntu:~$ nx cert-fix
```

The repair: refreshes the CA bundle → runs `apt-get update` with
**proof of success** (exit code + absence of failure signatures +
populated lists) → falls back to signed HTTP only when TLS genuinely
cannot work → repairs dpkg → installs `ca-certificates`,
`ubuntu-keyring`, `curl`, `wget` → regenerates the CA bundle →
restores HTTPS → verifies everything. A missing `noxs.sources` file is
self-healed from the canonical definition.

## Verify the result

```console
noxs@ubuntu:~$ noxs status            # certificates + apt state rows
noxs@ubuntu:~$ noxs ubuntu status     # keyring + package index
```

Both should show `OK`.

## Logs

Every run writes an auditable transcript to
`~/.noxs/logs/cert-fix-<timestamp>.txt`; the summary box at the end
points to it.

## Why signed-HTTP fallback is safe

Repository metadata stays GPG-authenticated
(`Signed-By: ubuntu-archive-keyring.gpg`) regardless of transport —
unauthenticated packages are still rejected by apt. HTTP is used only
during the repair window and only when HTTPS fails its proof check;
it is never a silent downgrade.
