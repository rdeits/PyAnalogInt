#PyAnalogInt
Analog integers in Python. By Robin Deits. 

License: MIT License

Inspired by: [http://weegen.home.xs4all.nl/eelis/analogliterals.xhtml](http://weegen.home.xs4all.nl/eelis/analogliterals.xhtml) by Eelis. 


Usage:

    >>> from analogInt import *
    >>> (I-I) == 1
    True
    >>> (I--I) == 2
    True
    >>> (I---I) == 2
    False
    >>> (I---I) == 3
    True
    >>> (I---I) + (I--I)
    (I-----I)
    >>> (I-----I) - (I--I)
    (I---I)
    >>> (I---I) * (I----I)
    (I---I
     |   l
     |   l
     |   l
     |   l
     |---I)
    >>> (I----I) * (I---I)
    (I----I
     |    l
     |    l
     |    l
     |----I)
    >>> r = (I----I) * (I---I)
    >>> r
    (I----I
     |    l
     |    l
     |    l
     |----I)
    >>> r.width
    (I----I)
    >>> r.height
    (I---I)
    >>> r / (I---I)
    (I----I)
    >>> (I---I)**2
    (I---I
     |   l
     |   l
     |   l
     |---I)
