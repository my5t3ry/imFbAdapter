import logging
import os
import random

import term

from fb.graph_api import GraphAPI

log = logging.getLogger('my5t3ry.imFbAdapter.service.FacebookDumpTask')


class FacebookDumpTask(object):
    def __init__(self, config_service):
        self.config = config_service
        self.graph = None
        self.auth_token = self.config.get("accessToken")
        self.init_graph_api(self.config.get("accessToken"))

    def do(self):
        if len(os.listdir(self.config.get("tmpPicDir"))) > 1:
            file = random.choice(os.listdir(self.config.get("tmpPicDir")))
            file_path = os.path.join(self.config.get("tmpPicDir"), file)
            try:
                self.graph.get(self.config.get("postPath"))
                self.graph.post(
                    path=self.config.get("postPath"),
                    source=open(file_path, 'rb'),
                    message=random.choice(self.config.get("postMessages")))
                log.info("posted file: '" + file + "'")
            except:
                log.info("\n\n\n\n=== facebook post failed! auth_token is expired please check https://developers.facebook.com/tools/accesstoken/ an obtain long term token ===\n\n\n\n")
    pass

    def init_graph_api(self, auth_token):
        self.graph = GraphAPI(auth_token)

    pass

    def validate(self):
        term.writeLine('Validating Facebook credentials...', term.green)
        try:
            self.graph.get(self.config.get("postPath"))
            term.writeLine('OK', term.green)
        except:
            term.writeLine('Facebook credentials and/or auth_token invalid. No facebook posts possible. Check => https://developers.facebook.com/tools/accesstoken/', term.red)

    pass

    def get_new_interval(self):
        if self.config.get("enableRandomFacebookPostingInterval"):
            return random.randint(self.config.get("minFacebookPostingInterval"), self.config.get("maxFacebookPostingInterval"))
        else:
            return self.config.get("facebookDumpInterval")

    pass
