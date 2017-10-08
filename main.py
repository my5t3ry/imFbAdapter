import logging
import sys
import time
from service.configService import ConfigService
from service.schedulerService import SchedulerService
from service.task.facebookDumpTask import FacebookDumpTask
from service.task.imgurScraperTask import ImgurScraperTask


def init (args):
    config_service = ConfigService()
    initLogging(config_service)
    imgur_scrape_scheduler = SchedulerService(config_service.config, ImgurScraperTask(config_service.config), config_service.config.get("imgurScrapeInterval"))
    facebook_dump_scheduler = SchedulerService(config_service.config, FacebookDumpTask(config_service.config), config_service.config.get("facebookDumpInterval"));
    imgur_scrape_scheduler.run()
    facebook_dump_scheduler.run()
    while True:
        time.sleep(1)


def initLogging(config_service):
    log = logging.getLogger('apscheduler.executors.default')
    logging.basicConfig()
    log.setLevel(config_service.config.get("loglevel"))
    log.info("== imFbAdapter 0.1 ==")
    log.info("imgur scrape interval config: '" + str(config_service.config.get("imgurScrapeInterval")) + "'")
    log.info("facebook dump interval config: '" + str(config_service.config.get("facebookDumpInterval")) + "'")
    log.info("== dump the shit away ==>")


if __name__ == '__main__':
    init(sys.argv)
