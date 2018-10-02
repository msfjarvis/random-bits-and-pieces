#!/usr/bin/env bash

# Copyright (C) Harsh Shandilya <msfjarvis@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only
# Execute in the root dir of https://github.com/material-components/material-components-android
# Replace /home/msfjarvis/aosip/frameworks/support with path to https://android.googlesource.com/frameworks/support/+/android-8.0.0_r1

# shellcheck disable=SC2035,SC2044,SC2061
# SC2035: Use ./*glob* or -- *glob* so names with dashes won't become options.
# SC2044: For loops over find output are fragile. Use find -exec or a while read loop.
# SC2061: Quote the parameter to -name so the shell won't interpret it.

for item in $(find lib/java/ -type f -name *.java); do
    name=$(basename "$item")
    if [[ "$name" == 'package-info.java' ]]; then
        continue
    fi
    fqcn=$(echo "$item" | sed -e 's/lib\/java\///' -e 's/\.java//' -e 's/\//\./g')
    normal=$(find /home/msfjarvis/aosip/frameworks/support -name "$name" | sed -e 's/.*\/android/android/' -e 's/.*\/java\///' -e 's/lib\/java\///' -e 's/\.java//' -e 's/\//\./g' | grep -v 'tests' | awk '{print $1}')
    if [[ -z "$normal" || "$normal" = "* *" ]]; then
        continue
    fi
    echo "$normal,$fqcn" >> material-class-mapping.csv
done
