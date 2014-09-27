# -*- encoding: utf-8 -*-

import re


class Parser:
    def __init__(self):
        self.instances = []
        self.current_instance = None

    def feed(self, lines):
        if not lines:
            return False

        self.current_instance = HRSSInstance()

        self._parse_jobs_number(lines[0])
        self._parse_machines_number(lines[0])
        self._parse_initialization_time(lines[2])
        self._parse_setup_times(lines[4])

        self.instances.append(self.current_instance)

        return self.instances

    def _parse_jobs_number(self, line):
        line = line.split('  ')[0]
        match = re.match('Number of jobs: ([0-9]+)', line)
        self.current_instance.jobs_number = int(match.group(1))

    def _parse_machines_number(self, line):
        line = line.split('  ')[1]
        match = re.match('Number of machines: ([0-9]+)', line)
        self.current_instance.machines_number = int(match.group(1))

    def _parse_initialization_time(self, line):
        match = re.match('Initialization time: ([0-9]+)', line)
        self.current_instance.initialization_time = int(match.group(1))

    def _parse_setup_times(self, line):
        line = line.replace('Setup times: ', '')
        times = line.split(' ')
        self.current_instance.setup_times = [int(t) for t in times if t != '']


class HRSSInstance:
    def __init__(self, initialization_time=0, machines_number=0, setup_times=None,
        processing_times=None, jobs_number=0):
        self.jobs_number = jobs_number
        self.initialization_time = initialization_time
        self.machines_number = machines_number
        self.setup_times = setup_times
        self.processing_times = processing_times
