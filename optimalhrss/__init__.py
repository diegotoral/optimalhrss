# -*- encoding: utf-8 -*-

import sys

from options import Options


if __name__ == '__main__':
    options = Options()
    args = options.parse(sys.argv[1:])

    print 'Optimal HRSS'
