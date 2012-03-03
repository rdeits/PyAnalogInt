"""
Analog integers in Python. By Robin Deits. 
License: MIT License

Inspired by: http://weegen.home.xs4all.nl/eelis/analogliterals.xhtml by Eelis. 


Usage:
>>> from analogInt import *
>>> (I----I) / (I--I)
(I--I)
>>> (I--I) + (I--I)
(I----I)
>>> (I---I) - (I-I)
(I--I)
>>> (I---I) / (II)
ZeroDivisionError: integer division or modulo by zero
>>> (I---I) ** (I--I)
(I---------I)
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
    def __str__(self):
        return "(I" + ''.join(['-' for i in range(self)]) + "I)"
    def __repr__(self):
        return self.__str__()

I = HalfAnalogInt(0)
II = FullAnalogInt(0)


"""
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
