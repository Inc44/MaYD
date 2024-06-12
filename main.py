import argparse
from logic import process_list

parser = argparse.ArgumentParser(
    description="Downloads audio and video from a provided URL and processes media files"
)
parser.add_argument(
    "url",
    type=str,
    help="Enter the URL of the playlist or media to download, e.g., 'https://music.youtube.com/playlist?list=OLAK5uy_lN9u5OOPNcOJtKWUm5ts7gIixbBnDvagQ'",
)
parser.add_argument(
    "--cookiefile",
    type=str,
    default="cookies.txt",
    help="Path to the cookie file for authentication, defaults to 'cookies.txt'",
)
arguments = parser.parse_args()

url = arguments.url
cookiefile = arguments.cookiefile

process_list(url, cookiefile)
