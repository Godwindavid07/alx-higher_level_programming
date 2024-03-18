#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Creates a new list with an element replaced at a specific index, without modifying the original list.
    Args:
    my_list (list): The original list.
    idx (int): The index of the element to replace.
    element (any): The new element.
    Returns:
    list: A new list with the replacement, or a copy of the original list
    if the index is invalid.
    """
    new_list = my_list.copy()
    if 0 <= idx < len(my_list):
        new_list[idx] = element
