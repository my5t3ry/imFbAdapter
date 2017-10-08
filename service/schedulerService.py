import logging

from apscheduler.scheduler import Scheduler, EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

log = logging.getLogger('my5t3ry.imFbAdapter.service.ScheduleService')


class SchedulerService(object):
    def __init__(self, config, task):
        self.config = config
        self.task = task
        self.task_thread = Scheduler()
        self.job = None

    def run(self):
        self.task_thread.add_listener(self.reconfigure_interval, EVENT_JOB_EXECUTED)
        self.task_thread.add_listener(self.reconfigure_interval, EVENT_JOB_ERROR)
        self.reconfigure_interval(None)

    def reconfigure_interval(self, event):
        if event:
            self.task_thread.unschedule_job(event.job)
            self.task_thread.shutdown(wait=False)
        new_interval = self.task.get_new_interval()
        log.debug("=== interval for job:'" + str(self.task) + "' set to :'" + str(new_interval) + "'===")
        self.job = self.task_thread.add_interval_job(self.task.do, seconds=new_interval)
        self.task_thread.start()
        pass
