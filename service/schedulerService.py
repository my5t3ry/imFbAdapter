from apscheduler.schedulers.background import BackgroundScheduler


class SchedulerService(object):
    def __init__(self, config, task):
        self.config = config
        self.task = task

    def run(self):
        apsched = BackgroundScheduler()
        apsched.add_job(self.task.do, trigger='interval', seconds=self.config.get("facebookDumpInterval"))
        apsched.start()


