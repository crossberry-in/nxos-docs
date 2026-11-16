# Network Errors

Network problems surface in four places: apt, package downloads, the
AI gateway and the browser. Diagnose with:

```console
noxs@ubuntu:~$ noxs network status
```

(transport, metered state and validation summary — no identifiers are
reported).

## apt / TLS failures

`certificate verification failed`, TLS handshake errors, empty package
lists → [`nx cert-fix`](../cli/cert-fix.md). The repair rebuilds the
CA bundle and verifies apt really succeeded before restoring HTTPS.
See [Certificate errors](certificate-errors.md).

## Downloads stall or fail

- Package downloads use two attempts with resume support; a failed
  retry continues where it stopped — just re-run the command.
- `MIRROR_UNAVAILABLE` is normal when the optional mirror is down:
  the installer falls back to official URLs. See
  [mirror architecture](../architecture/mirror.md).
- Metered networks: downloads honor Android's metered state; connect
  to unmetered Wi-Fi for large artifacts.

## AI gateway errors

`timeout` / `unavailable` / `rate_limit` / `auth` — the mapped codes
and fixes are in [AI troubleshooting](../ai/troubleshooting.md).

## Browser / web windows

`nx ow` uses the system WebView stack — network errors are the
page's/WebView's own (DNS, captive portals). URL validation blocks
non-web schemes; see [Native browser](../cli/web-browser.md).

## DNS problems

`/etc/resolv.conf` is written by Noxs at setup. After unusual network
changes:

```console
noxs@ubuntu:~$ cat /etc/resolv.conf
noxs@ubuntu:~$ getent hosts ports.ubuntu.com
```

If resolution fails on a working network, re-run the environment's
DNS configuration by restarting the session, or report it.

## VPN / Tor mode

`nx vpn status` / `nx vpn test` report the Tor daemon state; routing
applies to **new** shells after `nx vpn on`. See
[`nx` VPN commands](../cli/nx.md#web-and-vpn).
