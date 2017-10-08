import os

from imgur import ImgurScraper, AlbumFetcher


class ImgurScraperTask(object):
    def __init__(self, config_service):
        self.config = config_service

    def do(self):
        iscraper = ImgurScraper()
        galleryLinks = iscraper.imgur_urls(self.config.get("rootImgurGallery"))
        for galleryLink in galleryLinks:
            album_fetcher = AlbumFetcher(galleryLink)
            album_fetcher.save_images(self.config.get("tmpPicDir"))
    pass

