from argparse import ArgumentParser
from logic import process_list
from multiprocessing import freeze_support

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
    arguments = parser.parse_args()

    url = arguments.url
    cookiefile = arguments.cookiefile

    process_list(url, cookiefile)
