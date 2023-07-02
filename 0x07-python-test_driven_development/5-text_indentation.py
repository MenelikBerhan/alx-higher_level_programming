#!/usr/bin/python3
"""
'5-text_indentation' module.

This module contains `text_indentation` function that prints text
by adding two newlines after special characters.
"""


def text_indentation(text):
    """Prints text by adding two newlines after each `.`, `?` and `:`

    Args:
        text (`str`): text to be printed

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    printable = ""
    text_len = len(str(text))
    index = 0
    while index < text_len:
        line = ""
        while index < text_len and text[index] == " ":
            index += 1
        if index == text_len:
            break
        while index < text_len and text[index] not in ".?:\n":
            line += text[index]
            index += 1
        if index == text_len:
            print(line.strip(), end="")
            break
        if text[index] == '\n':
            print(line.strip())
            index += 1
            continue
        if text[index] in ".?:":
            line += text[index] + '\n\n'
            print(line, end="")
            index += 1
            continue
