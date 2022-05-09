"""
input/ output read file in json, text format
"""
import json


def read_json(path):
    """
    read json files
    """
    with open(path, "r") as file_content:
        my_file = json.load(file_content)
    return my_file


def read_text(path):
    """
    read text files
    """
    with open(path, "r") as file_content:
        my_file = file_content.read()
    return my_file

def write_json(path, content):
    """
    write json files
    """
    with open(path, "x") as js_file:
        json.dump(content, js_file, indent=4)
