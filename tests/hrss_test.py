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
    def setUp(self):
        self.job = Job(1, 1)
        self.name = 'MachineGun'
        self.machine = Machine(self.name)
        self.machine.configure_job(self.job)

    def test_has_a_name(self):
        self.assertEqual(self.machine.name, self.name)

    def test_cup_time_defaults_to_zero(self):
        self.assertEqual(self.machine.cpu_time, 0)

    def test_inicialization_updates_cpu_time(self):
        self.machine.initialize()
        self.assertEqual(self.machine.cpu_time, self.job.initialization_time)

    def test_setup_updates_cpu_time(self):
        self.machine.setup()
        self.assertEqual(self.machine.cpu_time, self.job.setup_time)

    def test_process_updates_cpu_time(self):
        self.machine.process()
        self.assertEqual(self.machine.cpu_time, 1)
