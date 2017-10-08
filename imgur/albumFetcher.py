import logging
import math
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

import log as log

log = logging.getLogger('my5t3ry.imFbAdapter.imgur.albumFetcher')


class FetchException(Exception):
    def __init__(self, msg=False):
        self.msg = msg


class AlbumFetcher:
    def __init__(self, album_url):
        self.album_url = album_url
        self.image_callbacks = []
        self.complete_callbacks = []

        match = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", album_url)
        if not match:
            raise FetchException("URL must be a valid Imgur Album")

        self.protocol = match.group(1)
        self.album_key = match.group(4)
        full_list_URL = "http://imgur.com/gallery/" + self.album_key

        try:
            context = ssl._create_unverified_context()
            self.response = urllib.request.urlopen(url=full_list_URL, context=context)
            response_code = self.response.getcode()
        except Exception as e:
            self.response = False
            response_code = e.code

        if not self.response or self.response.getcode() != 200:
            raise FetchException("Error reading Imgur: Error Code %d" % response_code)
        html = self.response.read().decode('utf-8')
        self.imageIDs = re.findall('.*?{"hash":"([a-zA-Z0-9]+)".*?"ext":"(\.[a-zA-Z0-9]+)".*?', html)

        self.cnt = Counter()
        for i in self.imageIDs:
            self.cnt[i[1]] += 1

    def num_images(self):
        return len(self.imageIDs)

    def list_extensions(self):
        return self.cnt.most_common()

    def album_key(self):
        return self.album_key

    def on_image_download(self, callback):
        self.image_callbacks.append(callback)

    def on_complete(self, callback):
        self.complete_callbacks.append(callback)

    def save_images(self, foldername=False):
        if foldername:
            albumFolder = foldername
        else:
            albumFolder = self.album_key

        if not os.path.exists(albumFolder):
            os.makedirs(albumFolder)

        for (counter, image) in enumerate(self.imageIDs, start=1):
            image_url = "http://i.imgur.com/" + image[0] + image[1]
            prefix = "%0*d-" % (
                int(math.ceil(math.log(len(self.imageIDs) + 1, 10))),
                counter
            )
            path = os.path.join(albumFolder, prefix + image[0] + image[1])
            for fn in self.image_callbacks:
                fn(counter, image_url, path)
            if os.path.isfile(path):
                log.info("Skipping, already exists.")
            else:
                try:
                    urllib.request.urlretrieve(image_url, path)
                    log.info("Fetched:' " + image[0] + image[1])
                except Exception as e:
                    log.info("Download failed.")
                    os.remove(path)
        for fn in self.complete_callbacks:
            fn()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        exit()

    try:
        downloader = AlbumFetcher(args[1])
        log.info(("Found {0} images in album".format(downloader.num_images())))

        for i in downloader.list_extensions():
            log.info(("Found {0} files with {1} extension".format(i[1], i[0])))


        def print_image_progress(index, url, dest):
            log.info(("Downloading Image %d" % index))
            log.info(("    %s >> %s" % (url, dest)))


        downloader.on_image_download(print_image_progress)


        def all_done():
            print("")
            print("Done!")


        downloader.on_complete(all_done)
        if len(args) == 3:
            albumFolder = args[2]
        else:
            albumFolder = False
        downloader.save_images(albumFolder)
        exit()

    except FetchException as e:
        log.info(("Error: " + e.msg))
        print("")
        print("How to use")
        print("=============")
        exit(1)
