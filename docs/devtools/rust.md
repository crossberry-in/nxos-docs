# Rust

Rust installs from the Ubuntu repositories. The NX package system also
scaffolds Rust projects with a multi-arch release workflow.

## Install (apt)

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y rustc cargo
noxs@ubuntu:~$ rustc --version && cargo --version
```

*(Version = what Ubuntu 24.04 ships; check `apt policy rustc`. For a
newer toolchain, rustup is a normal guest download but is not a
documented Noxs feature.)*

## Building a crate

```console
noxs@ubuntu:~$ cargo new hello && cd hello
noxs@ubuntu:~$ cargo build --release
noxs@ubuntu:~$ ./target/release/hello
```

`cargo` works normally: crates.io fetches over HTTPS, builds compile
natively for aarch64, and `cargo run/test` behave as on a desktop.

## Rust package projects with the NX system

```console
noxs@ubuntu:~$ nx pkg init mytool --rust
noxs@ubuntu:~$ cd mytool && nx pkg build
```

The template ships `Cargo.toml`, `src/main.rs` and GitHub Actions
automation that cross-builds `x86_64`, `aarch64` and `armv7` release
artifacts (`<name>.nx.pkg.<version>.<arch>.tar.xz` + sha256 sidecars) —
see [Development workflows](workflows.md).

## Notes

- First builds are CPU-heavy; keep `-j` modest on thermally limited
  devices.
- `cargo install` works for tools with published aarch64 support;
  source builds need the same toolchain.
