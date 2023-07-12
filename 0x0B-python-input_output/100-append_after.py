#!/usr/bin/python3
"""Module containing `append_after` function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text `new_string` to a file named `filename`,
    after each line containing a specific string `new_string`"""
    # first read the whole file string
    with open(filename, encoding="utf-8") as my_file:
        content = my_file.readlines()
    new = []
    for line in content:
        new.append(line)
        if search_string in line:
            new.append(new_string)
    # new_content = ''.join(new)
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.writelines(new)
        # my_file.write(new_content)
