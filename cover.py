from base64 import b64encode
from ffmpeg import FFmpeg
from mutagen.flac import Picture
from mutagen.mp4 import MP4, MP4Cover
from mutagen.oggopus import OggOpus
from os import path
from subprocess import run
from yt_dlp import YoutubeDL


def download_video(url):
    ydl_opts = {
        "quiet": True,
        "ignoreerrors": True,
        "outtmpl": "%(id)s.%(ext)s",
        "format": "(1080x1080)/699/399/335/303/616/248/299/216/137/170",
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)
    return video_path


def extract_cover(video_path):
    cover_path = path.splitext(video_path)[0] + ".png"
    ffmpeg = FFmpeg().option("y").input(video_path).output(cover_path, vframes=1)
    ffmpeg.execute()
    return cover_path


def compress_cover(video_path):
    run(
        [
            "ect",
            "-9",
            "-strip",
            "-quiet",
            "--strict",
            "--mt-file",
            video_path,
        ]
    )


def apply_cover(audio_path, cover_path):
    extension = path.splitext(audio_path)[1]
    if extension == ".m4a":
        apply_cover_m4a(audio_path, cover_path)
    elif extension == ".opus":
        apply_cover_opus(audio_path, cover_path)


def apply_cover_m4a(audio_path, cover_path):
    with open(cover_path, "rb") as artwork:
        file = MP4(audio_path)
        file["covr"] = [MP4Cover(artwork.read(), imageformat=MP4Cover.FORMAT_PNG)]
        file.save()


def apply_cover_opus(audio_path, cover_path):
    with open(cover_path, "rb") as artwork:
        file = OggOpus(audio_path)
        pic = Picture()
        pic.data = artwork.read()
        pic.type = 3
        pic.mime = "image/png"
        file["metadata_block_picture"] = b64encode(pic.write()).decode("ascii")
        file.save()
