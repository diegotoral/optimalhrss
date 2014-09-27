# -*- encoding: utf8 -*-

import random


class Schedule(object):
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def __getitem__(self, index):
        return self.order[index]

    def __setitem__(self, index, value):
        self.order.insert(index, value)

    def __iter__(self):
        return iter(self.order)

    def add(self, job, machine):
        self.order.append((job, machine))


class RandomSchedule(Schedule):
    def __init__(self, jobs, machines):
        super(self.__class__, self).__init__()
        self.jobs, self.machines = jobs, machines

        self._build_schedule()

    def _build_schedule(self):
        random.shuffle(self.jobs)
        self.order = map(lambda j: (j, random.choice(self.machines)), self.jobs)
