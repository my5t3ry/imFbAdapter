import logging


class ConfigService:
    def __init__(self):
        pass

    def get_config(self):
        return self.config

    config = {
        'author_email': 'sascha.bast@gmail.com',
        'version': '0.1',

        'imgurScrapeInterval': 900,  # seconds
        'facebookDumpInterval': 40,
        'imgurURL': 'https://imgur.com/gallery/hot/viral/',
        'loglevel': logging.DEBUG,
        'rootImgurGallery': "https://imgur.com/gallery/hot/viral/",
        'tmpPicDir': './tmpDump/',
        'facebookUser': 'sash@mischkonsum.org',
        'facebookPass': 'Qicklink1',
        'postPath': 'me/photos',
        'accessToken': 'EAAEAavJWEMABAE5BigMEe7u8mXsXtvGg4jYX1xWxEk32ArJ2LVcDCPVFzXOUnEaCH2yjj1eKQvHMDmjLwg7FQIrJFPwTypbKVB5HjUdi7s2URZAuyzWDkiWl3vJfmz9Yf9oEottvAgoNzA0raxKndAXZB8x3kZBa4h7mTZCZAfIYVQzYaSWEf7ABqY85zZBtd6s9qwDWXaQgZDZD',
        'postMessages': [
            "imgur x posting bot test -> ",
            "imgur x posting bot test -> ",
            "imgur x posting bot test ->",
        ]
    }
