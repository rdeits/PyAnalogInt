#PyAnalogInt
Analog integers in Python. By Robin Deits. 

License: MIT License

Inspired by: [http://weegen.home.xs4all.nl/eelis/analogliterals.xhtml](http://weegen.home.xs4all.nl/eelis/analogliterals.xhtml) by Eelis. 


Usage:

    >>> from analogInt import *
	>>> (I---I) == 3
	True
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
