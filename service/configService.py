import logging


class ConfigService:
    def __init__(self):
        pass

    def get_config(self):
        return self.config

    config = {
        'imgurScrapeInterval': 100,  #seconds
        'facebookDumpInterval': 1000,
        'author_email': 'sascha.bast@gmail.com',
        'version': '0.1',
        'imgurURL': 'https://imgur.com/gallery/hot/viral/',
        'loglevel': logging.DEBUG,
        'rootImgurGallery': "https://imgur.com/gallery/hot/viral/",
        'tmpPicDir': './tmpDump/',
        'facebookUser': 'XXXXX',
        'facebookPass': 'XXXXX',
        'postPath': 'me/photos',
        'accessToken': 'EAACEdEose0cBAMvNDxhhZCbq0WWqTPVxhjnNg0D8XeSGwjkwpSjF577JGpVWVdLxduIbRqDAbkUITFb4MFhxaOfwZCjUcPvBjILftLhekiYYdZAuOqnHA3JkzLG8FfrgNyWhiHT6ixYjaRZBuI9sQKNDUW6RfFncffEnwFaiMXJvHWTPrTSqTOP5tiCigxB3LrZAhrgn6MgZDZD',
        'postMessages': [
            "Sea impetus platonem ",
            "impetus nec an ",
            "haedrum et, eirmod",
        ]
    }
