#!/usr/bin/python3
"""Module containing `append_write` function"""


def append_write(filename="", text=""):
    """Appends the contents of `text` to file named `filename`
    and returns number of characters written"""
    with open(filename, "a", encoding="utf-8") as myfile:
        nChar = myfile.write(text)
    return nChar
