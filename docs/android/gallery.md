# Gallery and Camera Integration

## Photo Picker — `noxs document gallery`

```console
noxs@ubuntu:~$ noxs document gallery
noxs@ubuntu:~$ noxs document gallery ~/Pictures/my-shot.jpg
```

Opens Android's **Photo Picker** (permissionless on Android 13+;
graceful fallback on older releases) and saves the chosen photo inside
Noxs. Default destination:
`~/Pictures/noxs-gallery-<timestamp>.jpg`.

## Camera — `noxs camera`

```console
noxs@ubuntu:~$ noxs camera
noxs@ubuntu:~$ noxs camera ~/Pictures/photo.jpg
```

Opens the native camera app; the capture is handed back and saved to
the destination (default `~/Pictures/noxs-<timestamp>.jpg`).

**Permission**: `android.permission.CAMERA` — declared by the app and
requested at first use through Android's runtime dialog. Captures reach
the terminal only after you take them; nothing runs in the background.

## Media permissions on Android 13+

Media imports can use the scoped `READ_MEDIA_IMAGES` /
`READ_MEDIA_VIDEO` permissions (asked on use). On older Android
versions the legacy read permission path applies. See
[App permissions](app-permissions.md#nx-android-integration-permissions).

## Saving and sharing results

```console
noxs@ubuntu:~$ noxs share ~/Pictures/photo.jpg   # Android Sharesheet
noxs@ubuntu:~$ noxs document export ~/Pictures/photo.jpg
```

## Privacy notes

- Photo Picker selections are per-item grants — Noxs never gains bulk
  media access through it.
- Camera captures and gallery picks are written into your guest home
  and exposed only through
  [Noxs Linux Home](internal-storage.md).
