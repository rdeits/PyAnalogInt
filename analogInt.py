"""
Usage:
>>> from analogInt import *
>>> (II)
>>> (I------I)
>>> (I--I) + (I--I)
"""


class HalfAnalogInt(int):
    def __sub__(self, x):
        return FullAnalogInt(int.__add__(int.__sub__(self, x),1))
    def __neg__(self):
        return HalfAnalogInt(int.__sub__(self, 1))

class FullAnalogInt(int):
    def __add__(self, x):
        return FullAnalogInt(int.__add__(self, x))
    def __sub__(self, x):
        return FullAnalogInt(int.__sub__(self, x))
    def __str__(self):
        return "(I" + ''.join(['-' for i in range(self)]) + "I)"
    def __repr__(self):
        return self.__str__()
    def __mul__(self, other):
        return FullAnalogInt(int.__mul__(self, other))
    def __floordiv__(self, other):
        return FullAnalogInt(int.__floordiv__(self, other))
    def __mod__(self, other):
        return FullAnalogInt(int.__mod__(self, other))
    def __divmod__(self, other):
        return FullAnalogInt(int.__divmod__(self, other))
    def __pow__(self, other, modulo=None):
        return FullAnalogInt(int.__pow__(self, other, modulo))
    def __div__(self, other):
        return FullAnalogInt(int.__div__(self, other))
    def __truediv__(self, other):
        return FullAnalogInt(int.__truediv__(self, other))

I = HalfAnalogInt(0)
II = FullAnalogInt(0)
