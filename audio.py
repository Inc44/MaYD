from ffmpeg import FFmpeg
from os import path, remove, rename
from yt_dlp import YoutubeDL


def download_audio(
    url, format="338/258/328/325/380/327/141/774/256/251/140", cookiefile="cookies.txt"
):
    ydl_opts = {
        "quiet": True,
        "ignoreerrors": True,
        "outtmpl": "%(id)s.%(ext)s",
        "format": format,
        "cookiefile": cookiefile,
        # C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --disable-features=LockProfileCookieDatabase
        # "cookiesfrombrowser": ("edge",),
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # In order to use python-ffmpeg instead of subprocess with a double hyphen (`--`) before the output name, original paths are left stripped
        original_audio_path = ydl.prepare_filename(info)
        audio_path = original_audio_path.lstrip("-")
        if audio_path != original_audio_path:
            rename(original_audio_path, audio_path)
    return audio_path


def container_audio(audio_path):
    extension = path.splitext(audio_path)[1]
    if extension == ".webm":
        audio_path_opus = path.splitext(audio_path)[0] + ".opus"
        ffmpeg = (
            FFmpeg().option("y").input(audio_path).output(audio_path_opus, c="copy")
        )
        ffmpeg.execute()
        remove(audio_path)
        audio_path = audio_path_opus
    audio_container_path = audio_path
    return audio_container_path
