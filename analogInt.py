"""
Usage:
>>> from analogInt import *
>>> (II)
>>> (I------I)
>>> (I--I) + (I--I)
"""


class AnalogInt(int):
    def __sub__(self, x):
        return int(x)
    def __neg__(self):
        return AnalogInt(self + 1)

I = AnalogInt(1)
II = 0
