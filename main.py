import logging
import sys
import time
import os
from service.configService import ConfigService
from service.schedulerService import SchedulerService
from service.task.facebookDumpTask import FacebookDumpTask
from service.task.imgurScraperTask import ImgurScraperTask


def init(args):
    config_service = ConfigService()
    init_logging(config_service)
    imgur_scrape_scheduler = SchedulerService(config_service.config, ImgurScraperTask(config_service.config))
    facebook_dump_scheduler = SchedulerService(config_service.config, FacebookDumpTask(config_service.config))
    imgur_scrape_scheduler.run()
    facebook_dump_scheduler.run()
    while True:
        time.sleep(1)


def init_logging(config_service):
    log = logging.getLogger('my5t3ry.main')
    logging.basicConfig(level=config_service.config.get("loglevel"))
    log.info("=== imgur scrape interval config: '" + str(config_service.config.get("imgurScrapeInterval")) + "' ===")
    log.info("=== facebook dump interval config: '" + str(config_service.config.get("facebookDumpInterval")) + "' ===")
    log.info("=== current pile consists of '" + str(len(os.listdir(config_service.config.get("tmpPicDir"))))+ "' items ===")
    log.info("=== dump the shit away ===>\n\n")


if __name__ == '__main__':
    init(sys.argv)
