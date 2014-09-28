# -*- encoding: utf-8 -*-

import unittest

from optimalhrss.timer import CodeTimer


class TestCodeTimer(unittest.TestCase):
    def setUp(self):
        self.timer = CodeTimer()

    def test_start_defaults_to_zero(self):
        self.assertEqual(self.timer.start, 0)

    def test_end_defaults_to_zero(self):
        self.assertEqual(self.timer.end, 0)

    def test_secs_defaults_to_zero(self):
        self.assertEqual(self.timer.secs, 0)

    def test_msecs_defaults_to_zero(self):
        self.assertEqual(self.timer.msecs, 0)

    def test_updates_start_on_enter(self):
        with CodeTimer() as t:
            self.assertNotEqual(t.start, 0)

    def test_updates_end_on_exit(self):
        with CodeTimer() as t:
            pass

        self.assertNotEqual(t.end, 0)

    def test_updates_secs_on_exit(self):
        with CodeTimer() as t:
            pass

        self.assertNotEqual(t.secs, 0)

    def test_updates_msecs_on_exit(self):
        with CodeTimer() as t:
            pass

        self.assertNotEqual(t.msecs, 0)
