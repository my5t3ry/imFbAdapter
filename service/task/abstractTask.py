class AbstractTask(object):
    def do(self, job_func, *args, **kwargs):
        raise NotImplementedError('subclasses must override exec()!')

    def get_new_interval(self):
        pass
