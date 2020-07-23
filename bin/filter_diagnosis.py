#!/usr/bin/env python3
import pandas as pd
import copy
import json
import sys
import os

main_json = sys.argv[1]
output_json = sys.argv[2]



if len(sys.argv) != 3:
    print("usage: {} <main_json> <output_json> <disease_ontology_map>".format(
        sys.argv[0]))
    exit(1)


# Read main report file
with open(main_json) as r:
    report = json.load(r)


# Filter report based on diagnosis

def filter_on_diagnosis(section):
    filtered_section = [
        d for d in section if d["seen_in_diagnosis"] != False]
    return filtered_section


report["driver_table"] = filter_on_diagnosis(report["driver_table"])
report["direct_pharm_table"] = filter_on_diagnosis(
    report["direct_pharm_table"])
report["pharm_table"] = filter_on_diagnosis(report["pharm_table"])


with open(output_json, "w") as o:
    json.dump(report, o, indent=4)

