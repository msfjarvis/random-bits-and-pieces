#!/usr/bin/env python3

# Copyright (C) Harsh Shandilya <msfjarvis@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

"""
Small script that quickly verifies if localizations
for a given project are in sync with the source file
"""

import argparse
import os
from xml.etree import ElementTree


def search_files(directory='.', file_name='strings.xml'):
    """
    Method to traverse through a given directory to find files
    """
    output = []
    file_name = file_name.lower()
    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                output.append(os.path.join(root, file))
    return output


def analyze_translations(source_file, tolerance, remove_incomplete):
    """
    The site of the actual functioning of the script
    """
    file_to_process = source_file.split("/")[-1]
    source = open(source_file, 'r').read()
    xml_root = ElementTree.fromstring(source)
    strings = xml_root.findall('string')
    total_strings = len(strings)
    print("Strings in original file: %s" % total_strings)
    for found_file in search_files(file_name=file_to_process):
        if found_file == "./%s" % source_file:
            continue
        source = open(found_file, 'r').read()
        xml_root = ElementTree.fromstring(source)
        strings = xml_root.findall('string')
        percentage = (len(strings) / total_strings) * 100
        if percentage < tolerance:
            print("%s is not in sync with source files, missing %s strings"
                  % (found_file, total_strings - len(strings)))
            if remove_incomplete:
                print("Deleting")
                os.remove(found_file)
        else:
            print("%s in sync with source files" % found_file)


def main():
    """
    Boilerplate for argument parsing
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Source file to compare against; it's assumed "
                                               "the localizations exist with the same file name.",
                        type=str, default="app/src/main/res/values/strings.xml")
    parser.add_argument("-t", "--tolerance", help="Percentage of missing strings that are "
                                                  "allowed before we consider deletion",
                        type=int, default=100)
    parser.add_argument("-r", "--remove", help="Remove localizations not in the tolerance range",
                        action="store_true")
    args = parser.parse_args()

    analyze_translations(args.source, args.tolerance, args.remove)


if __name__ == '__main__':
    main()
