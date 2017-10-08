import json


class ConfigService:
    def __init__(self):
        with open('./config.cfg') as data_file:
            self.config = json.load(data_file)

        pass

    def get_config(self):
        return self.config
