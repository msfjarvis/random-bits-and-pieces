#!/usr/bin/env python3.7
"""
Script to convert a settings.json database from the Kernel Adiutor app's data
into an Android init script for inclusion in custom ramdisks
"""

import json
import os

import sys

DEBUG = False
FINAL_RC_SCRIPT = []
if not os.path.exists("settings.json"):
    print("settings.json doesn't exist!")
    sys.exit(255)

SETTINGS_JSON = json.load(open("settings.json", "r"))
for entry in SETTINGS_JSON["database"]:
    category = entry["category"]
    if category == "cpu_onboot":
        setting = json.loads(entry["setting"].replace("#", "").replace(r"\"", '"'))
        for i in range(setting["min"], setting["max"] + 1):
            FINAL_RC_SCRIPT.append(
                "write {} {}".format(setting["path"] % i, setting["value"])
            )
    else:
        setting = entry["setting"]
        setting_raw = setting.split(">")
        if len(setting_raw) == 1:
            if (
                setting_raw[0].find("chmod") != -1
                or setting_raw[0].find("sysctl") != -1
            ):
                FINAL_RC_SCRIPT.append(setting_raw[0])
                continue
            print("{0} could not be parsed".format(setting))
        try:
            value = setting_raw[0].split("'")[1]
            sysfs_path = setting_raw[1].replace(" ", "")
            if DEBUG:
                print(value, sysfs_path)
            FINAL_RC_SCRIPT.append("write {} '{}'".format(sysfs_path, value))
        except IndexError:
            continue

with open("init.output.rc", "w") as output:
    for line in FINAL_RC_SCRIPT:
        output.write(line + os.linesep)
