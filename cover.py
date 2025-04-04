from base64 import b64encode
from ffmpeg import FFmpeg
from mutagen.flac import Picture
from mutagen.mp4 import MP4, MP4Cover
from mutagen.oggopus import OggOpus
from os import path, remove, rename
from subprocess import run
from yt_dlp import YoutubeDL


def download_video(
	url,
	format="699/399/335/303/356/616/248/299/216/137/170/698/398/334/302/612/247/298/136/169",
	cookiefile="cookies.txt",
):
	ydl_opts = {
		"quiet": True,
		"ignoreerrors": True,
		"outtmpl": "%(id)s.%(ext)s",
		"format": format,
		"cookiefile": cookiefile,
		# C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --disable-features=LockProfileCookieDatabase
		# "cookiesfrombrowser": ("edge", "firefox"),
	}
	with YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=True)
		# In order to use python-ffmpeg instead of subprocess with a double hyphen (`--`) before the output name, original paths are left stripped
		original_video_path = ydl.prepare_filename(info)
		video_path = original_video_path.lstrip("-")
		if video_path != original_video_path:
			rename(original_video_path, video_path)
	return video_path


def extract_cover(video_path):
	cover_path = path.splitext(video_path)[0] + ".png"
	ffmpeg = FFmpeg().option("y").input(video_path).output(cover_path, vframes=1)
	ffmpeg.execute()
	remove(video_path)
	return cover_path


def compress_cover(cover_path):
	run(
		[
			"ect",
			"-9",
			"-strip",
			"-quiet",
			"--strict",
			"--mt-file",
			cover_path,
		]
	)
	return cover_path


def apply_cover(audio_container_path, cover_path):
	extension = path.splitext(audio_container_path)[1]
	if extension == ".m4a":
		apply_cover_m4a(audio_container_path, cover_path)
	elif extension == ".opus":
		apply_cover_opus(audio_container_path, cover_path)
	remove(cover_path)
	return audio_container_path


def apply_cover_m4a(audio_container_path, cover_path):
	with open(cover_path, "rb") as artwork:
		file = MP4(audio_container_path)
		file["covr"] = [MP4Cover(artwork.read(), imageformat=MP4Cover.FORMAT_PNG)]
		file.save()


def apply_cover_opus(audio_container_path, cover_path):
	with open(cover_path, "rb") as artwork:
		file = OggOpus(audio_container_path)
		pic = Picture()
		pic.data = artwork.read()
		pic.type = 3
		pic.mime = "image/png"
		file["metadata_block_picture"] = b64encode(pic.write()).decode("ascii")
		file.save()
