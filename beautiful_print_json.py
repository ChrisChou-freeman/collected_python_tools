# -*- coding: utf-8 -*-
import json
import pprint
import sys

def beautiful_print(json_data):
    python_obj = json.loads(json_data)
    pprint.PrettyPrinter().pprint(python_obj)

if __name__ == "__main__":
    json_data = input("json data>>")
    beautiful_print(json_data)
