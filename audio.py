from ffmpeg import FFmpeg
from os import path, remove
from yt_dlp import YoutubeDL


def download_audio(
    url, format="338/258/328/325/380/327/141/774/256/251", cookiefile="cookies.txt"
):
    ydl_opts = {
        "quiet": True,
        "ignoreerrors": True,
        "outtmpl": "%(id)s.%(ext)s",
        "format": format,
        "cookiefile": cookiefile,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        audio_path = ydl.prepare_filename(info)
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
