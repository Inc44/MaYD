from os import rename, path


def create_file_name(info_list_item):
    invalid_file_name_chars = '\/:*?"<>|'
    # IDK how somebody managed to fuck up that and string None value
    if info_list_item["artist"] != "None":
        file_name = f"""{info_list_item["artist"]} - {info_list_item["album"]} - {info_list_item["track"]} - {info_list_item["release_year"]} [{info_list_item["id"]}]"""
    else:
        file_name = f"""{info_list_item["title"]} - {info_list_item["upload_date"][:4]} [{info_list_item["id"]}]"""
    file_name = file_name.replace(" - None", "")
    file_name = "".join(
        char if char not in invalid_file_name_chars else "" for char in file_name
    )
    # A more sustainable solution is needed, but this is very rare as it has only happened twice in the past for over 8000 files
    if len(file_name) > 241:
        file_name = f"""{file_name[:224]}... [{info_list_item["id"]}]"""
    return file_name


def create_file_path(audio_path, file_name):
    dir_path, ext = path.splitext(audio_path)
    file_path = f"""{dir_path[:-11]}{file_name}{ext}"""
    rename(audio_path, file_path)
    return file_path
