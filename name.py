from os import rename, path


def create_file_name(info_list_entry):
    invalid_file_name_chars = '\/:*?"<>|'
    if info_list_entry["artist"] != "NA":
        file_name = f"""{info_list_entry["artist"]} - {info_list_entry["album"]} - {info_list_entry["track"]} - {info_list_entry["release_year"]} [{info_list_entry["id"]}]"""
    else:
        file_name = f"""{info_list_entry["title"]} - {info_list_entry["upload_date"][:4]} [{info_list_entry["id"]}]"""
    file_name = file_name.replace(" - NA", "")
    file_name = "".join(
        char if char not in invalid_file_name_chars else "" for char in file_name
    )
    # needs a more sustainable solution (happened only twice in the past)
    if len(file_name) > 241:
        file_name = f"""{file_name[:224]}... [{info_list_entry["id"]}]"""
    return file_name


def create_file_path(audio_path, file_name):
    dir_path, ext = path.splitext(audio_path)
    file_path = f"{dir_path[:-11]}{file_name}{ext}"
    rename(audio_path, file_path)
    return file_path
