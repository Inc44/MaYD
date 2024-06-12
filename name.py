from os import rename, path


def create_file_name(info_list_item):
    invalid_file_name_chars = '\/:*?"<>|'
    if info_list_item["artist"] != "NA":
        file_name = f"""{info_list_item["artist"]} - {info_list_item["album"]} - {info_list_item["track"]} - {info_list_item["release_year"]} [{info_list_item["id"]}]"""
    else:
        file_name = f"""{info_list_item["title"]} - {info_list_item["upload_date"][:4]} [{info_list_item["id"]}]"""
    file_name = file_name.replace(" - NA", "")
    file_name = "".join(
        char if char not in invalid_file_name_chars else "" for char in file_name
    )
    # needs a more sustainable solution (happened only twice in the past)
    if len(file_name) > 241:
        file_name = f"""{file_name[:224]}... [{info_list_item["id"]}]"""
    return file_name


def create_file_path(audio_path, file_name):
    dir_path, ext = path.splitext(audio_path)
    file_path = f"{dir_path[:-11]}{file_name}{ext}"
    rename(audio_path, file_path)
    return file_path
