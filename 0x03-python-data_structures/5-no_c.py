#!/usr/bin/python3
def no_c(my_string):
    """Removes all 'c' and 'C' characters from a string.
    Args:
    my_string (str): The string to remove 'c' and 'C' characters from.
    Returns:
    str: The new string without 'c' or 'C' characters.
    """
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
            return new_string
