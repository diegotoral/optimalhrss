# -*- encoding: utf-8 -*-

import re


class Parser:
    def __init__(self):
        self.instance = HRSSInstance()

    def feed(self, input):
        if not input:
            return False

        self._parse_initialization_time(input)
        self._parse_machines_number(input)
        self._parse_setup_times(input)

        return self.instance

    def _parse_initialization_time(self, line):
        # match = re.match('Initialization time: ([0-9]+)', line)
        self.instance.initialization_time = 1 #match.group(1)

    def _parse_machines_number(self, line):
        self.instance.machines_number = 2

    def _parse_setup_times(self, line):
        self.instance.setup_times = ['7', '7', '10', '12', '14', '33', '23', '29', '7', '20']


class HRSSInstance:
    def __init__(self, initialization_time=0, machines_number=0, setup_times=None, processing_times=None):
        self.initialization_time = initialization_time
        self.machines_number = machines_number
        self.setup_times = setup_times
        self.processing_times = processing_times
