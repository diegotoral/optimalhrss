# -*- encoding: utf-8 -*-

import time


class CodeTimer(object):
    def __init__(self):
        self.start = self.end = self.secs = self.msecs = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
