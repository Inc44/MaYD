from info import download_info, get_info_path, playlist_info, write_info, read_info
from url import get_download_domain, create_download_url
from audio import download_audio, container_audio
from cover import download_video, extract_cover, compress_cover, apply_cover
from name import create_file_name, create_file_path
from multiprocessing import Pool, cpu_count


def process_list(url, cookiefile, serial_processing=True):
    info = download_info(url, cookiefile=cookiefile)

    # Add "move" or "download directly to Desktop/specified directory" option for all downloaded content

    # Fix multiprocessing: downloading a YouTube music playlist will download premium audio (141) only on the first track

    # Implement cookie file copy or browser extraction due to relatively quick expiration

    # Add the following code to the yt_dlp/utils/networking.py file at the beginning of the HTTPHeaderDict class (lines 59 to 64):
    # from yt_dlp.utils.networking import HTTPHeaderDict
    # def __new__(cls, *args, **kwargs):
    #     obj = super().__new__(cls, *args, **kwargs)
    #     obj.data = {}
    #     return obj

    # Faster debugging
    # import pickle
    # with open('info.pkl', 'wb') as file:
    #     pickle.dump(info, file)
    # with open('info.pkl', 'rb') as file:
    #     info = pickle.load(file)

    playlist_path, database_path = get_info_path(info)
    playlist_path = playlist_info(info, playlist_path)
    database_path = write_info(info, database_path)
    info_list = read_info(database_path)

    download_domain = get_download_domain(url)

    if serial_processing:
        for info_list_item in info_list:
            process_list_item(info_list_item, download_domain, cookiefile)
    else:
        info_list_process_count = min(len(info_list), cpu_count())
        with Pool(info_list_process_count) as pool:
            pool.starmap(
                process_list_item,
                [(item, download_domain, cookiefile) for item in info_list],
            )


def process_list_item(info_list_item, download_domain, cookiefile):
    id = info_list_item["id"]

    download_url = create_download_url(download_domain, id)

    audio_path = download_audio(download_url, cookiefile=cookiefile)
    audio_container_path = container_audio(audio_path)

    file_name, is_music = create_file_name(info_list_item)

    if is_music:
        video_path = download_video(download_url, cookiefile=cookiefile)
        cover_path = extract_cover(video_path)
        cover_path = compress_cover(cover_path)
        audio_container_path = apply_cover(audio_container_path, cover_path)

    file_path = create_file_path(audio_container_path, file_name)

    return file_path
