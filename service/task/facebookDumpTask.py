import logging
import os
import random

from fb.graph_api import GraphAPI

log = logging.getLogger('my5t3ry.imFbAdapter.service.FacebookDumpTask')


class FacebookDumpTask(object):
    def __init__(self, config_service):
        self.config = config_service

    def do(self):
        if len(os.listdir(self.config.get("tmpPicDir"))) > 1:
            file = random.choice(os.listdir(self.config.get("tmpPicDir")))
            file_path = os.path.join(self.config.get("tmpPicDir"), file)
            graph = GraphAPI(self.config.get("accessToken"))
            graph.get(self.config.get("postPath"))
            log.info("posted file: '" + file + "'")
            graph.post(
                path=self.config.get("postPath"),
                source=open(file_path, 'rb'),
                message=random.choice(self.config.get("postMessages")))

    pass

    def get_new_interval(self):
        if self.config.get("enableRandomFacebookPostingInterval"):
            return random.randint(self.config.get("minFacebookPostingInterval"), self.config.get("maxFacebookPostingInterval"))
        else:
            return self.config.get("facebookDumpInterval")
        pass
