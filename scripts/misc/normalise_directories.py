#!/usr/bin/env python3.5
"""
Script to strip metadata from file and folder names
"""

import os
import re

ROOT_DIR = '.'

for dirName, subdirList, fileList, in os.walk(ROOT_DIR):
    for dname in subdirList:
        normalised_dir = dirName + '/' + re.sub(' ', '.', re.sub(r' \(.*', '', dname))
        source_dir = dirName + '/' + dname
        if normalised_dir not in (dname, source_dir):
            print('{} -> {}'.format(source_dir, normalised_dir))
            os.rename(source_dir, normalised_dir)
