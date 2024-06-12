from yt_dlp import YoutubeDL


def download_info(url):
    ydl_opts = {
        "quiet": True,
        "ignoreerrors": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def get_info_path(info, playlist_path="main.playlist", database_path="main.database"):
    entries = info.get("entries", [info])
    albums = [entry.get("album") for entry in entries]
    first_album = albums[0]
    if all(album == first_album for album in albums):
        playlist_path = f"""{first_album}.playlist"""
        database_path = f"""{first_album}.database"""
    return playlist_path, database_path


def playlist_info(info, playlist_path="main.playlist"):
    entries = info.get("entries", [info])
    ids = [entry.get("id") for entry in entries if entry.get("id")]
    playlist_link = f'www.youtube.com/watch_videos?video_ids={",".join(ids)}'
    with open(playlist_path, "w", encoding="utf-8") as f:
        f.write(playlist_link)
    return playlist_path


def write_info(info, database_path="main.database"):
    entries = info.get("entries", [info])
    database = [
        {
            "id": entry.get("id"),
            "title": entry.get("title"),
            "upload_date": entry.get("upload_date"),
            "artist": entry.get("artist"),
            "album": entry.get("album"),
            "track": entry.get("track"),
            "release_year": entry.get("release_year"),
        }
        for entry in entries
    ]
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
