#!/usr/bin/python3
""" create an object from json file """

import json


def load_from_json_file(filename):
    """ creates an object """
    with open(filename) as file:
        object = json.load(file)
        return object
