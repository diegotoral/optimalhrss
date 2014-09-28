# -*- encoding: utf-8 -*-

import sys
from argparse import ArgumentParser


class Options(object):
    def __init__(self):
        self.parser = ArgumentParser(prog='optimalhrss')

        self._add_arguments(self.parser)

    def parse(self, argv):
        return self.parser.parse_args(argv)

    def _add_arguments(self, parser):
        parser.add_argument('file', help='file with instances to load')
