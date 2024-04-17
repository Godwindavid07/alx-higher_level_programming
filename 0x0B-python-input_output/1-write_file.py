#!/usr/bin/python3
"""defines a func that writes to a file"""
def write_file(filename="", text=""):
    """write a string to txt file
    Args:
    filename (str): name if the file to write text
    text (str): the text to write
    Returns:
    NO of characters written.
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        return (myfile.write(text))
