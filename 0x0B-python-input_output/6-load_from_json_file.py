#!/usr/bin/python3
"""Module containing `load_from_json_file` function"""
import json


def load_from_json_file(filename):
    """`object`: Creates and returns an Object from a `JSON` file"""
    with open(filename, "r", encoding="utf-8") as my_file:
        new_obj = json.load(my_file)
    return new_obj
