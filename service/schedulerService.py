from apscheduler.schedulers.background import BackgroundScheduler


class SchedulerService(object):
    def __init__(self, config, task, interval):
        self.config = config
        self.intervall = interval
        self.task = task

    def run(self):
        apsched = BackgroundScheduler()
        apsched.add_job(self.task.do, 'interval', seconds=self.intervall)
        apsched.start()
