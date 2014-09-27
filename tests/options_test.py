# -*- encoding: utf-8 -*-

import unittest

from optimalhrss.options import Options


class TestOptions(unittest.TestCase):
    def test_parses_a_filename(self):
        filename = 'filename.txt'
        options = Options().parse([filename])
        self.assertEquals(options.file, filename)
