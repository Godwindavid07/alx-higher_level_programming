#!/usr/bin/python3
"""defines a file_ appending function"""
def append_write(filename="", text=""):
    """Appends a string to end of UTF-8 txt file.
    Args:
    filename (str): name of the file to append.
    text (str): string to append.
    Reurns:
    numbers of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return (myfile.write(text))
