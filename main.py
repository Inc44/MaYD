from info import download_info, get_info_path, playlist_info, write_info, read_info
from url import get_download_domain, create_download_url
from audio import download_audio, container_audio
from cover import download_video, extract_cover, compress_cover, apply_cover
from name import create_file_name, create_file_path


url = (
    "https://music.youtube.com/playlist?list=OLAK5uy_lN9u5OOPNcOJtKWUm5ts7gIixbBnDvagQ"
)

info = download_info(url)
playlist_path, database_path = get_info_path(info)
playlist_path = playlist_info(info, playlist_path)
database_path = write_info(info, database_path)
info_list = read_info(database_path)

for info_list_item in info_list:
    id = info_list_item["id"]

    download_domain = get_download_domain(url)
    download_url = create_download_url(download_domain, id)

    audio_path = download_audio(download_url)
    audio_container_path = container_audio(audio_path)

    video_path = download_video(download_url)
    cover_path = extract_cover(video_path)
    cover_path = compress_cover(cover_path)
    audio_path = apply_cover(audio_container_path, cover_path)

    file_name = create_file_name(info_list_item)
    file_path = create_file_path(audio_path, file_name)