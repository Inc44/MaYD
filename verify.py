from argparse import ArgumentParser
import os
import re


def extract_ids_from_playlist(playlist_path):
    ids = set()
    with open(playlist_path, "r", encoding="utf-8") as f:
        for line in f:
            if "video_ids=" in line:
                video_ids = line.strip().split("video_ids=")[1]
                ids.update(video_ids.split(","))
    return ids


def get_video_files(directory):
    video_files = {}
    id_pattern = re.compile(r"\[([a-zA-Z0-9_-]{11})\]\.(m4a|opus)$")
    for file in os.listdir(directory):
        match = id_pattern.search(file)
        if match:
            video_id = match.group(1)
            video_files[video_id] = file
    return video_files


def verify_files(playlist_path, directory):
    playlist_ids = extract_ids_from_playlist(playlist_path)
    video_files = get_video_files(directory)
    print(f"\nFound {len(playlist_ids)} IDs in playlist")
    print(f"Found {len(video_files)} files in directory")
    missing_files = playlist_ids - video_files.keys()
    extra_files = video_files.keys() - playlist_ids
    if missing_files:
        print("\nMissing files:")
        for vid_id in sorted(missing_files):
            print(f"- {vid_id}")
    if extra_files:
        print("\nExtra files:")
        for vid_id in sorted(extra_files):
            print(f"- {video_files[vid_id]}")
    if not missing_files and not extra_files:
        print("\nAll files match! ✓")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Verify that files in directory match IDs in main.playlist"
    )
    parser.add_argument(
        "playlist",
        type=str,
        help="Path to main.playlist file",
    )
    parser.add_argument(
        "directory",
        type=str,
        default=".",
        help="Directory containing the media files",
    )
    args = parser.parse_args()
    verify_files(args.playlist, args.directory)
