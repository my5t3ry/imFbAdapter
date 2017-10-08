from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


class SchedulerService(object):
    def __init__(self, config, task, interval):
        self.config = config
        self.intervall = interval
        self.task = task

    def run(self):
        apsched = BackgroundScheduler()
        trigger = IntervalTrigger(seconds=self.intervall)
        apsched.add_job(self.task.do, trigger)
        apsched.start()
