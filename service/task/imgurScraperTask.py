import os
import term

from imgur.albumFetcher import AlbumFetcher
from imgur.imgurScraper import ImgurScraper


class ImgurScraperTask(object):
    def __init__(self, config_service):
        self.config = config_service

    def do(self):
        imgur_scraper = ImgurScraper(self.config)
        gallery_links = imgur_scraper.imgur_urls()
        for galleryLink in gallery_links:
            album_fetcher = AlbumFetcher(galleryLink)
            album_fetcher.save_images(self.config.get("tmpPicDir"))

    pass

    def get_new_interval(self):
        return self.config.get("imgurScrapeInterval")

    pass

    def validate(self):
        term.writeLine('Validating imgur media dump ...', term.green)
        try:
            str(len(os.listdir(self.config.get("tmpPicDir"))))
            term.writeLine('OK', term.green)
        except Exception as e:
            term.writeLine('Media folder not readable', term.red)
