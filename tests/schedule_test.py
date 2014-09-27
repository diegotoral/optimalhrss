# -*- encoding: utf8 -*-

import unittest

from optimalhrss.schedules import Schedule, RandomSchedule


class TestSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = Schedule()

    def test_has_an_order_list(self):
        self.assertIsNotNone(self.schedule.order)

    def test_get_an_item(self):
        self.schedule.order = [1]
        self.assertEqual(self.schedule[0], 1)

    def test_set_an_item(self):
        self.schedule[0] = True
        self.assertTrue(self.schedule[0])

    def test_add_an_item(self):
        expected = ('job', 'machine')
        self.schedule.add(expected[0], expected[1])
        self.assertEqual(self.schedule[0], expected)

    def test_schedule_length(self):
        self.assertEqual(len(self.schedule), 0)

    def test_iterate_over_a_schedule(self):
        self.schedule.order = [1, 1, 1]
        for o in self.schedule:
            self.assertTrue(o)


class TestRandomSchedule(unittest.TestCase):
    def test_create_a_random_schedule(self):
        jobs, machines = range(1, 10), ['A', 'B']
        self.schedule = RandomSchedule(jobs, machines)
        self.assertEqual(len(self.schedule), len(jobs))
