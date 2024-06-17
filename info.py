from yt_dlp import YoutubeDL


def download_info(url, cookiefile="cookies.txt"):
    ydl_opts = {
        "quiet": True,
        "ignoreerrors": True,
        "cookiefile": cookiefile,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def get_info_path(info, playlist_path="main.playlist", database_path="main.database"):
    entries = info.get("entries", [info])
    previous_album = None
    same_album = True

    for entry in entries:
        if entry is None:
            raise ValueError("Unavailable video or YouTube Music Premium only error")
        current_album = entry.get("album")
        if previous_album is not None and current_album != previous_album:
            same_album = False
            break
        previous_album = current_album

    if same_album and previous_album is not None:
        playlist_path = f"""{previous_album}.playlist"""
        database_path = f"""{previous_album}.database"""

    return playlist_path, database_path


def playlist_info(info, playlist_path="main.playlist"):
    entries = info.get("entries", [info])
    ids = []
    for entry in entries:
        if entry is None:
            raise ValueError("Unavailable video or YouTube Music Premium only error")
        id = entry.get("id")
        ids.append(id)
    playlist_link = f"""www.youtube.com/watch_videos?video_ids={",".join(ids)}"""
    with open(playlist_path, "w", encoding="utf-8") as f:
        for id in range(0, len(ids), 50):
            playlist_chunk = ids[id : id + 50]
            playlist_link = (
                f"www.youtube.com/watch_videos?video_ids={','.join(playlist_chunk)}"
            )
            f.write(playlist_link + "\n")
    return playlist_path


def write_info(info, database_path="main.database"):
    entries = info.get("entries", [info])
    database = []
    for entry in entries:
        if entry is None:
            raise ValueError("Unavailable video or YouTube Music Premium only error")
        database.append(
            {
                "id": entry.get("id"),
                "title": entry.get("title"),
                "upload_date": entry.get("upload_date"),
                "artist": entry.get("artist"),
                "album": entry.get("album"),
                "track": entry.get("track"),
                "release_year": entry.get("release_year"),
            }
        )
    lines = [
        "%(id)s\t%(title)s\t%(upload_date)s\t%(artist)s\t%(album)s\t%(track)s\t%(release_year)s"
        % entry
        for entry in database
    ]
    with open(database_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return database_path


def read_info(database_path="main.database"):
    info_list = []
    with open(database_path, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.strip().split("\t")
            info_list.append(
                {
                    "id": fields[0],
                    "title": fields[1],
                    "upload_date": fields[2],
                    "artist": fields[3],
                    "album": fields[4],
                    "track": fields[5],
                    "release_year": fields[6],
                }
            )
    return info_list
