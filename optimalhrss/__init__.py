# -*- encoding: utf-8 -*-

import sys

from options import Options
from instance import Parser


if __name__ == '__main__':
    options = Options()
    args = options.parse(sys.argv[1:])

    _file = open(args.file, 'r')

    if _file:
        parser = Parser()
        instances = parser.feed(_file.readlines())

    print 'Optimal HRSS'
