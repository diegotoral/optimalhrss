# -*- encoding: utf-8 -*-

import unittest

from fixtures import load_fixture
from optimalhrss.instance import Parser, HRSSInstance


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.instance_data = load_fixture('instance:simple')
        self.instances = self.parser.feed(self.instance_data)
        self.first_instance = self.instances[0]

    def tearDown(self):
        del self.parser

    def test_feed_with_an_invalid_input(self):
        self.assertFalse(self.parser.feed([]))

    def test_feed_with_valid_input(self):
        self.assertTrue(len(self.instances) > 0)

    def test_feed_parses_the_jobs_number(self):
        self.assertEqual(self.first_instance.jobs_number, 10)

    def test_feed_parses_the_initialization_time(self):
        self.assertEqual(self.first_instance.initialization_time, 1)

    def test_feed_parses_the_machines_number(self):
        self.assertEqual(self.first_instance.machines_number, 2)

    def test_feed_parses_the_setup_times_list(self):
        expected = [7, 7, 10, 12, 14, 33, 23, 29, 7, 20]
        self.assertEqual(self.first_instance.setup_times, expected)


class TestInstanceHRSS(unittest.TestCase):
    def setUp(self):
        self.hrss = HRSSInstance()

    def test_jobs_number_defaults_to_zero(self):
        self.assertEqual(self.hrss.jobs_number, 0)

    def test_initialization_time_defaults_to_zero(self):
        self.assertEqual(self.hrss.initialization_time, 0)

    def test_machines_number_defaults_to_zero(self):
        self.assertEqual(self.hrss.machines_number, 0)

    def test_setup_times_defaults_to_none(self):
        self.assertEqual(self.hrss.setup_times, None)

    def test_processing_times_defaults_to_none(self):
        self.assertEqual(self.hrss.processing_times, None)

