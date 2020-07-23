#!/usr/bin/env python3
import pandas as pd
import copy
import json
import sys
import os


# Place holder, to be implemented

main_json = sys.argv[1]
output_json = sys.argv[2]


if len(sys.argv) != 3:
    print("usage: {} <main_json> <output_json> <disease_ontology_map>".format(
        sys.argv[0]))
    exit(1)


# Read main report file
with open(main_json) as r:
    report = json.load(r)



# Save the result
with open(output_json, "w") as o:
    json.dump(report, o, indent=4)