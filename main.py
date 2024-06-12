import argparse
from logic import process_list

parser = argparse.ArgumentParser(
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
