# -*- encoding: utf-8 -*-


__all__ = ('load_fixture')


FIXTURES = {

'instance:simple': """
Number of jobs: 10  Number of machines: 2

Initialization time: 1

Setup times: 7  7  10  12  14  33  23  29  7  20

Processing times: 196  137  185  131  183  151  182  160  156  151

-------------------------------------------------------------------------------
""".split('\n')

}


def load_fixture(fixture_name):
    return FIXTURES[fixture_name]
