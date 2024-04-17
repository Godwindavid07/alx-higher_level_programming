#!/usr/bin/python3

""" defines file reading func """

def read_file(filename=""):
    """Reads utf-8 text file and print its content
    Args:
    filename: the name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as myfile:
        print(myfile.read(), end="")
