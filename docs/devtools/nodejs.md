# Node.js and npm

Node.js and npm are not preinstalled; install them from the official
Ubuntu repositories (or NodeSource if you prefer specific majors).

## Install

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y nodejs npm
noxs@ubuntu:~$ node --version
noxs@ubuntu:~$ npm --version
```

*(Version output depends on what Ubuntu 24.04 ships at install time —
check `apt policy nodejs` for the candidate version.)*

## Using npm

```console
noxs@ubuntu:~$ mkdir demo && cd demo
noxs@ubuntu:~$ npm init -y
noxs@ubuntu:~$ npm install cowsay
noxs@ubuntu:~$ npx cowsay "hello from Noxs"
```

npm works normally inside the sandbox: package scripts run, local
`node_modules` resolve, and `npm run` drives builds. Note that
postinstall scripts behave like any guest process — they can touch the
sandbox filesystem, so install packages you trust.

## Node package projects with the NX system

`nx pkg init <name> --node` scaffolds a Node.js package with a release
workflow that publishes a **universal** `.nx.pkg` artifact:

```console
noxs@ubuntu:~$ nx pkg init mytool --node
noxs@ubuntu:~$ cd mytool && nx pkg build
```

See [Development workflows](workflows.md) for the full
author-and-publish loop.

## Notes and limits

- Native addon builds (`node-gyp`) need `build-essential` and
  `python3` — install both first.
- ARM64 is the target; prebuilt binaries must exist for `linux-arm64`,
  otherwise npm compiles from source.
- There is no nvm-style version manager preconfigured; multiple Node
  versions are not a documented Noxs feature.
