#!/usr/bin/python3
"""Module containing `read_file` function"""


def read_file(filename=""):
    """Reads a text file and prints its content to `stdout`"""
    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
