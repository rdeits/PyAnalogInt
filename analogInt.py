"""
Analog integers in Python. By Robin Deits. 
License: MIT License

Inspired by: http://weegen.home.xs4all.nl/eelis/analogliterals.xhtml by Eelis. 


Usage:
(see Readme.md)
"""


class OneDBuilder(int):
    def __sub__(self, x):
        return OneDAnalogInt(int.__add__(int.__sub__(self, x),1))
    def __neg__(self):
        return ZeroDAnalogInt(int.__sub__(self, 1))

class OneDAnalogInt(int):
    def __add__(self, x):
        return OneDAnalogInt(int.__add__(self, x))
    def __sub__(self, x):
        return OneDAnalogInt(int.__sub__(self, x))
    def __mul__(self, other):
        return TwoDAnalogInt(self, other)
    def __pow__(self, other, modulo=None):
        if other == 2:
            return TwoDAnalogInt(self, self)
        else:
            raise ValueError("I don't know how to do more than squaring") 
    def __str__(self):
        return "(I" + ''.join(['-' for i in range(self)]) + "I)"
    def __repr__(self):
        return self.__str__()
    def __or__(self, x):
        return TwoDAnalogInt(self)

class TwoDAnalogInt:
    def __init__(self, width, height=0):
        self.width = OneDAnalogInt(width)
        self.height = OneDAnalogInt(height)
    def __or__(self, x):
        self.height = self.height + 1
        return self
    def __str__(self):
        return ("(I" + ''.join(['-' for i in range(self.width)]) + "I" +
                ''.join(["\n |" + ''.join([' ' for i in range(self.width)]) + "l"
                           for j in range(self.height)]) +
                "\n |" + ''.join(['-' for i in range(self.width)]) + "I)")
    def __repr__(self):
        return self.__str__()
    def __div__(self, other):
        self.area = self.width.__int__() * self.height.__int__()
        if self.area % other != 0:
            raise ValueError("Non-integer division") 
        if isinstance(other, TwoDAnalogInt):
            raise ValueError("Can't divide rectangle by another rectangle")
        return OneDAnalogInt(self.area / other.__int__())

I = OneDBuilder(0)
l = TwoDAnalogInt(0)
II = OneDAnalogInt(0)


"""
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
