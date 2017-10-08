from imgur.albumFetcher import AlbumFetcher
from imgur.imgurScraper import ImgurScraper


class ImgurScraperTask(object):
    def __init__(self, config_service):
        self.config = config_service

    def do(self):
        imgur_scraper = ImgurScraper()
        gallery_links = imgur_scraper.imgur_urls(self.config.get("rootImgurGallery"))
        for galleryLink in gallery_links:
            album_fetcher = AlbumFetcher(galleryLink)
            album_fetcher.save_images(self.config.get("tmpPicDir"))
    pass

    def get_new_interval(self):
        return self.config.get("imgurScrapeInterval")
        pass

