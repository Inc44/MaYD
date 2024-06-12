from info import download_info, playlist_info, write_info, read_info
from audio import download_audio, container_audio
from cover import download_video, extract_cover, compress_cover, apply_cover
from name import create_file_name, create_file_path

url = "https://music.youtube.com/watch?v=4TLFaQWcqH8"

info = download_info(url)
playlist_path = playlist_info(info)
database_path = write_info(info)
info_list = read_info(database_path)

audio_path = download_audio(url)
audio_container_path = container_audio(audio_path)

video_path = download_video(url)
cover_path = extract_cover(video_path)
cover_path = compress_cover(cover_path)
audio_path = apply_cover(audio_container_path, cover_path)

info_list_entry = info_list[0]
file_name = create_file_name(info_list_entry)
file_path = create_file_path(audio_path, file_name)
