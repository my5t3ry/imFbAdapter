from apscheduler.scheduler import Scheduler


class SchedulerService(object):
    def __init__(self, config, task, interval):
        self.config = config
        self.intervall = interval
        self.task = task

    def run(self):
        apsched = Scheduler()
        apsched.add_interval_job(self.task.do, seconds=self.intervall)
        apsched.start()
