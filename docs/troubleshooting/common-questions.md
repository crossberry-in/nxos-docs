# Common Questions (Runtime)

Getting-started questions live in the
[FAQ](../getting-started/faq.md); this page answers runtime questions
that come up during daily use.

**Why is there no `noxs` command for X?**
Check `noxs help` first — many Android features are covered
([command map](../reference/cli-reference.md)). If something is really
missing, it is either unplanned or listed under
[planned features](../getting-started/introduction.md#available-experimental-planned-unsupported).

**Why does `nx setup` not exist?**
Environment setup is the app's setup flow
([Initial setup](../getting-started/initial-setup.md)). The CLI has no
setup command; `nx setup` falls through the forwarder to `noxs`, which
reports `unknown command`.

**Where are my files on the Android side?**
In any file picker under **Noxs Linux Home** — that is `/home/noxs` of
the active environment. See
[Internal storage](../android/internal-storage.md).

**Why can't I `cd` into a SAF-granted folder?**
SAF access is command-based by design, not a POSIX mount:
`noxs storage ls/get/put/…`. The direct `/sdcard` mount is the opt-in
exception — see [Storage access](../files/storage-access.md).

**Do app updates wipe my Linux files?**
No — the environment lives in app-private storage and survives app
updates. Resets and environment removal are the destructive actions,
and both are explicit.

**Does the terminal keep running in the background?**
With *Keep sessions alive in background* enabled, yes — see
[Sessions](../terminal/sessions.md) and
[Background execution](../android/background-execution.md).

**Can I automate things at session start?**
Yes — standard bash startup files (`~/.bashrc`, `~/.profile`); see
[Shell configuration](../terminal/shell-configuration.md). There is no
Noxs-specific hook system.

**How do I report a bug?**
<https://github.com/crossberry-in/noxs/issues> — include the command,
the exact error text and, for setup problems, the setup console
transcript.
