# -*- encoding: utf8 -*-


class Job(object):
    def __init__(self, setup_time, processing_time, initialization_time=1):
        self.setup_time, self.processing_time = setup_time, processing_time
        self.initialization_time = initialization_time


class Machine(object):
    def __init__(self, name):
        self.name, self.cpu_time, self.job = name, 0, None

    def configure_job(self, job):
        self.job = job

    def initialize(self):
        self.cpu_time += self.job.initialization_time

    def setup(self):
        self.cpu_time += self.job.setup_time

    def process(self):
        self.cpu_time += self.job.processing_time
