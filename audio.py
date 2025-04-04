from ffmpeg import FFmpeg
from os import environ, path, remove, rename
from yt_dlp import YoutubeDL


def download_audio(
	url, format="338/258/328/325/380/327/141/774/256/251/140", cookiefile="cookies.txt"
):
	cookie_options = {}
	if path.exists(cookiefile) and path.getsize(cookiefile) > 0:
		cookie_options["cookiefile"] = cookiefile
		print("cookiefile")
	else:
		try:
			cookie_options["cookiesfrombrowser"] = ("firefox", None)
			print("cookiefrombrowser firefox")
		except Exception:
			try:
				cookie_options["cookiesfrombrowser"] = ("edge", None)
				print("cookiefrombrowser edge")
			except Exception:
				print("no cookie")
	extractor_args = {}
	po_token = environ.get("PO_TOKEN")
	if po_token:
		extractor_args["extractor_args"] = {
			"youtube": {
				"po_token": f"web_music.gvs+{po_token},web_music.player+{po_token}"
			}
		}
	ydl_opts = {
		"quiet": True,
		"ignoreerrors": True,
		"outtmpl": "%(id)s.%(ext)s",
		"format": format,
		# C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --disable-features=LockProfileCookieDatabase
		**cookie_options,
		**extractor_args,
	}
	with YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=True)
		if info is None:
			raise ValueError(f"no info {url}")
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
