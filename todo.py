"""
cookie dir, default within/Desktop, netscape, .txt
playlist dir, default within/Desktop, link, .playlist
database dir, default within/Desktop, tsv,. database

invalid filename chars, \/:*?"<>|

%(id)s\t%(title)s\t%(upload_date)s\t%(artist)s\t%(album)s\t%(track)s\t%(release_year)s

https > http
music > www

https://youtube.com/watch?v=QrhcfjPFaEk
https://youtube.com/watch?v=WAyN4mQgl-4

--list-formats

yt-dlp --cookies cookies.txt --download-archive yt-dlp.list --ignore-errors --write-info-json --add-metadata --write-sub --sub-lang en,fr,ru,ua,ja --write-thumbnail --embed-thumbnail --extract-audio -f "338/258/328/325/380/774/327/141/256/251" "youtube.com/watch?v=QrhcfjPFaEk"

yt-dlp --write-description --write-comments --write-link --write-auto-subs --embed-subs --embed-thumbnail --embed-chapters --sponsorblock-mark all "youtube.com/watch?v=QrhcfjPFaEk"
"""
