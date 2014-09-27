# -*- encoding: utf8 -*-


class Job(object):
    def __init__(self, setup_time, processing_time, initialization_time=1):
        self.setup_time, self.processing_time = setup_time, processing_time
        self.initialization_time = initialization_time


class Machine(object):
    def __init__(self, name):
        self.name = name
