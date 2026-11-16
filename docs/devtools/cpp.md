# C/C++

Install the GNU toolchain from Ubuntu's repositories; the NX package
system additionally scaffolds CMake-based C++ projects with multi-arch
release automation.

## Install

```console
noxs@ubuntu:~$ sudo apt update
noxs@ubuntu:~$ sudo apt install -y build-essential gdb
noxs@ubuntu:~$ gcc --version && g++ --version && make --version
```

`build-essential` brings gcc, g++, make and libc headers.

## Compile and run

```console
noxs@ubuntu:~$ cat > hello.c <<'EOF'
#include <stdio.h>
int main(void) { printf("hello from Noxs\n"); return 0; }
EOF
noxs@ubuntu:~$ gcc hello.c -o hello && ./hello
```

For CMake projects:

```console
noxs@ubuntu:~$ sudo apt install -y cmake
noxs@ubuntu:~$ cmake -B build -S . && cmake --build build -j2
```

## C++ package projects with the NX system

```console
noxs@ubuntu:~$ nx pkg init mytool --cpp
noxs@ubuntu:~$ cd mytool && nx pkg build
```

The template ships `CMakeLists.txt`, `src/main.cpp` and GitHub Actions
automation that cross-builds `x86_64`, `aarch64` and `armv7` artifacts
(`<name>.nx.pkg.<version>.<arch>.tar.xz` + sha256 sidecars) — see
[Development workflows](workflows.md).

## Notes

- The target triple is aarch64-linux-gnu; apt-installed `-dev`
  libraries are the supported way to link system libs.
- Cross-compiling *for* other targets from the device is not a
  documented feature — multi-arch builds happen in GitHub Actions.
