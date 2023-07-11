#!/usr/bin/python3
"""Module containing `to_json_string` function"""
import json


def to_json_string(my_obj):
    """`str`: Returns the `JSON` representation of an object"""
    return json.dumps(my_obj)
