#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
import os
import json

save_to_json_f = __import__('5-save_to_json_file').save_to_json_file
load_from_json_f = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_json = []

if os.path.exists(filename):
    list_json = load_from_json_f(filename)

for i in range(1, len(sys.argv)):
    list_json.append(sys.argv[i])

save_to_json_f(list_json, filename)
