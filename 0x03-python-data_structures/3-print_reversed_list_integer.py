#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order,
    Args:
    my_list (list, optional): The list of integers to print. Defaults to [].
    """
    if my_list:
        for i in my_list[::-1]):
        print("{:d}".format(i))
