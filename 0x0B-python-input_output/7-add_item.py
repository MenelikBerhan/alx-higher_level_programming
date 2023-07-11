#!/usr/bin/python3
"""Module containing a script that adds all arguments to a Python list,
and then save them as a JSON representation to a file named `add_item.json`"""

import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    arg_list = load_from_json_file("add_item.json")
except Exception:
    arg_list = []

arg_list_new = []
i = 1
while i < len(sys.argv):
    arg_list_new.append(sys.argv[i])
    i += 1
arg_list.extend(arg_list_new)

save_to_json_file(arg_list, "add_item.json")
