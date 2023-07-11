#!/usr/bin/python3
"""Module containing `write_file` function"""


def write_file(filename="", text=""):
    """Writes contents of `text` to file named `filename`
    and returns number of characters written"""
    with open(filename, "w", encoding="utf-8") as myfile:
        nChar = myfile.write(text)
    return nChar
