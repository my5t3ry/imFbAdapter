import logging
import os
import random

from fb.graph_api import GraphAPI


class FacebookDumpTask(object):
    def __init__(self, config_service):
        self.config = config_service

    def do(self):
        if len(os.listdir(self.config.get("tmpPicDir"))) > 1:
            file = random.choice(os.listdir(self.config.get("tmpPicDir")))
            filePath = os.path.join(self.config.get("tmpPicDir"), file)
            graph = GraphAPI(self.config.get("accessToken"))
            graph.get(self.config.get("postPath"))
            graph.post(
                path=self.config.get("postPath"),
                source=open(filePath, 'rb'),
                message=random.choice(self.config.get("postMessages")))
            log.info("posted file: '" + file + "'")

    pass


log = logging.getLogger('my5t3ry.imFbAdapter.imgur.albumFetcher')
