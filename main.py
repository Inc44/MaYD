from argparse import ArgumentParser
from datetime import datetime
from logic import process_list
from multiprocessing import freeze_support
from os import chdir
from pathlib import Path

default_output_dir = Path.home() / "Desktop" / datetime.now().strftime("%Y%m%d_%H%M%S")

if __name__ == "__main__":
    freeze_support()
    parser = ArgumentParser(
        description="Downloads audio and video from a provided URL and processes media files"
    )
    parser.add_argument(
        "url",
        type=str,
        help="Enter the URL of the playlist or media to download",
    )
    parser.add_argument(
        "--cookiefile",
        type=str,
        default="cookies.txt",
        help="Path to the cookie file for authentication",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default=str(default_output_dir),
        help="Directory to save output to",
    )
    arguments = parser.parse_args()

    url = arguments.url
    cookiefile = arguments.cookiefile
    output_dir = arguments.output_dir

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    chdir(output_dir)
    process_list(url, cookiefile)
