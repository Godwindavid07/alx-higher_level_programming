#!/usr/bin/python3

def lookup(obj):
    """Returns a list of user-defined attributes and methods of an object."""
    result = []
    attrs = dir(obj)

    builtin_attrs = set(dir(type(obj)))
    for item in attrs:
        if not item.startswith('__') and item not in builtin_attrs:
            attribute = getattr(obj, item)
            if callable(attribute):
                result.append(item + '()')
            else:
                result.append(item)
                return result
