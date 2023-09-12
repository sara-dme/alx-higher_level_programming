#!/usr/bin/python3
"""script that adds all arguments to a list, and save them to a file"""
import sys


if __name__ == "__main__":
    save_to = __import__('5-save_to_json_file').save_to_json_file
    load_from = __import__('6-load_from_json_file').load_from_json_file

    try:
        lst = load_from("add_item.json")
    except FileNotFoundError:
        lst = []
    lst.extend(sys.argv[1:])
    save_to(lst, "add_item.json")
