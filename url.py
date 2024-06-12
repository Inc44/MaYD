from urllib.parse import urlparse


def get_download_domain(url, default_domain="https://www.youtube.com"):
    parsed_url = urlparse(url)
    valid_domains = [
        "m.youtube.com",
        "music.youtube.com",
        "www.youtube.com",
        "youtu.be",
        "youtube.com",
    ]
    if parsed_url.hostname in valid_domains:
        default_domain = f"{parsed_url.scheme}://{parsed_url.hostname}"
    return default_domain


def create_download_url(download_domain, id):
    download_url = f"{download_domain}/watch?v={id}"
    return download_url
