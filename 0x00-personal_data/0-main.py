#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__("filtered_logger").filter_datum

fields = ["password", "date_of_birth"]
messages = [
    (
        f"name=egg;email=eggmin@eggsample.com;"
        f"password=eggcellent;date_of_birth=12/12/1986;"
    ),
    (
        f"name=bob;email=bob@dylan.com;"
        f"password=bobbycool;date_of_birth=03/04/1993;"
    ),
]

for message in messages:
    print(filter_datum(fields, "xxx", message, ";"))
