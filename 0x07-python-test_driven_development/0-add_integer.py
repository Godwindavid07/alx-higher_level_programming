#!/usr/bin/python3
def add_integer(a, b=98):
    """ Returns the integer sum of a and b
    float arguments are typecasted to integer before addition is performed
    raises:
    TypeError: if either one of a or b is a non-integer and a non-float value.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
