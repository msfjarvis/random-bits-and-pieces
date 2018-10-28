#!/usr/bin/env python3.5
"""
Script to strip metadata from file and folder names
"""

import os
import re

ROOT_DIR = '.'

for dirName, subdirList, fileList, in os.walk(ROOT_DIR):
    for dname in subdirList:
        normalised_dir_name = dirName + '/' + re.sub(' ', '.', re.sub(r' \(.*', '', dname))
        if dname != normalised_dir_name:
            os.rename(dirName + '/' + dname, normalised_dir_name)
