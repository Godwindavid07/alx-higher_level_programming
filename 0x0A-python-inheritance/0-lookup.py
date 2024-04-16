#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the available attributes and methods.
    """

    result = []

    # Get the object's attributes using dir()
    attrs = dir(obj)

    # Iterate through attributes and filter them
    for item in attrs:
        # Exclude private and magic methods/attributes
        if not item.startswith('__'):
            # Check if it's a method (callable)
            attribute = getattr(obj, item)  # Get the actual attribute value
            if callable(attribute):
                result.append(item + '()')  # Indicate it's a method
            else:
                result.append(item)
    
    return result
