# -*- encoding: utf8 -*-

import unittest

from optimalhrss.hrss import Job, Machine


class TestJob(unittest.TestCase):
    def setUp(self):
        self.job = Job(1, 1)

    def test_setup_time(self):
        self.assertEqual(self.job.setup_time, 1)

    def test_processing_time(self):
        self.assertEqual(self.job.processing_time, 1)

    def test_initialization_time_defaults_to_one(self):
        self.assertEqual(self.job.initialization_time, 1)


class TestMachine(unittest.TestCase):
    def test_has_a_name(self):
        name = 'MachineGun'
        machine = Machine(name)
        self.assertEqual(machine.name, name)
