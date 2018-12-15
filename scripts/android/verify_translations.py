#!/usr/bin/env python3

"""
Small script that quickly verifies if localizations
for a given project are in sync with the source file
"""

# Copyright (C) Harsh Shandilya <msfjarvis@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import os
import sys
from xml.etree import ElementTree


def search_files(directory='.', file_name='strings.xml'):
    """
    Method to traverse through a given directory to find files
    """
    output = []
    file_name = file_name.lower()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_name):
                output.append(os.path.join(root, file))
    return output


def analyze_translations():
    """
    The site of the actual functioning of the script
    """
    source_file = sys.argv[1]
    file_to_process = source_file.split("/")[-1]
    source = open(source_file, 'r').read()
    xml_root = ElementTree.fromstring(source)
    strings = xml_root.findall('string')
    total_strings = len(strings)
    print("Strings in original file: %s" % total_strings)
    for found_file in search_files(file_name=file_to_process):
        source = open(found_file, 'r').read()
        xml_root = ElementTree.fromstring(source)
        strings = xml_root.findall('string')
        if total_strings != len(strings):
            print("%s is not fully in sync, missing %s strings"
                  % (found_file, total_strings - len(strings)))
            # os.remove(found_file)
        else:
            print("%s is fully in sync with source files" % found_file)


if len(sys.argv) == 1:
    print("Specify the source filename to begin")
    sys.exit(1)

analyze_translations()
