# -*- encoding: utf-8 -*-

import unittest

from fixtures import load_fixture
from optimalhrss.instance import Parser, HRSSInstance


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.instance_data = load_fixture('instance:simple')
        self.returned_instance = self.parser.feed(self.instance_data)

    def test_feed_with_an_invalid_input(self):
        self.assertFalse(self.parser.feed([]))

    def test_feed_with_valid_input(self):
        self.assertIsInstance(self.returned_instance, HRSSInstance)

    def test_feed_parses_the_initialization_time(self):
        self.assertEqual(self.returned_instance.initialization_time, 1)

    def test_feed_parses_the_machines_number(self):
        self.assertEqual(self.returned_instance.machines_number, 2)

    def test_feed_parses_the_setup_times_list(self):
        expected = ['7', '7', '10', '12', '14', '33', '23', '29', '7', '20']
        self.assertEqual(self.returned_instance.setup_times, expected)


class TestInstance(unittest.TestCase):
    def setUp(self):
        self.hrss = HRSSInstance()

    def test_initialization_time_defaults_to_zero(self):
        self.assertEqual(self.hrss.initialization_time, 0)

    def test_machines_number_defaults_to_zero(self):
        self.assertEqual(self.hrss.machines_number, 0)

    def test_setup_times_defaults_to_none(self):
        self.assertEqual(self.hrss.setup_times, None)

    def test_processing_times_defaults_to_none(self):
        self.assertEqual(self.hrss.processing_times, None)

