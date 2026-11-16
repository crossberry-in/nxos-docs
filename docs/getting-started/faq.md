# FAQ

**What is Noxs?**
An Android terminal app that runs a genuine **Ubuntu 24.04 LTS**
userspace inside the app sandbox via proot — with a real terminal, a
real editor, a package system and an Android integration layer.
[Introduction](introduction.md) has the full picture.

**Is Noxs based on another terminal app?**
No. Noxs is an original project (Apache-2.0) — clean-room
architecture, code, branding and assets. No third-party terminal code,
branding or assets are used.

**Does Noxs support Kali Linux?**
Not yet — Kali is a **planned** track. Today Noxs installs exactly one
environment: Ubuntu 24.04 LTS. Upgrading users' legacy Debian installs
are imported read-only. See
[Kali status](../environments/kali-installation.md).

**Does Noxs root my phone?**
No, and it never tries. `sudo` controls the Noxs environment only —
the welcome screen, terminal banner and Security screen state this
explicitly. See the [security model](../architecture/security.md).

**Why proot instead of chroot or a VM?**
chroot requires root or special kernel privileges most devices don't
grant apps. proot achieves path virtualization via ptrace entirely in
userland. proot environments do **not** provide the isolation of
hardware-backed virtualization — that limit is documented, not hidden,
in the [security model](../architecture/security.md).

**Why is /var/run "real"?**
It is a real directory *inside the app-private rootfs*. proot maps
`/var/run` requests into the rootfs tree, so sockets behave normally
while Android's actual `/var/run` is never touched. See
[Unix sockets](../architecture/unix-sockets.md).

**Where does code-server come from?**
`noxs code install` points to the official MIT-licensed code-server
release. Noxs never bundles or redistributes VS Code or code-server
binaries. See [Code Server](../devtools/code-server.md).

**Does it work offline?**
Yes, after the one-time bootstrap. Only package installation,
code-server download, AI gateways and the plugin store need the
network.

**Which permissions does Noxs need?**
None at install time. Storage (SAF), notifications, camera and the
opt-in direct mount are requested per feature, through Android's own
UI, and are revocable. Noxs holds **no SMS permission** — sending
hands the message to your own SMS app. See
[App permissions](../android/app-permissions.md).

**Is my data private?**
The Linux filesystem lives in the app's private storage. Device and
network reports are non-identifying summaries (no SSID, IMSI, phone
numbers, credentials). AI keys stay in your environment variables and
are never logged. See [API keys](../ai/api-keys.md) and the
[security model](../architecture/security.md).

**Is Noxs the same as NoxOS?**
No — different products. Noxs is the Android terminal; NoxOS is a
separate emulator track that Noxs can integrate with. See
[NoxOS Emulator](../architecture/noxos-emulator.md).

**Where do I report bugs?**
<https://github.com/crossberry-in/noxs/issues> — include the command
and exact error text. Docs issues go to
<https://github.com/crossberry-in/nxos-docs>.
