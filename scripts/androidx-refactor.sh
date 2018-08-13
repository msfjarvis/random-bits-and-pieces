#!/bin/bash

# Copyright (C) Harsh Shandilya <msfjarvis@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

[ -f androidx-class-mapping.csv ] || wget https://developer.android.com/topic/libraries/support-library/downloads/androidx-class-mapping.csv
sed -i '1d' androidx-class-mapping.csv # Remove the first line since it's not an actual class mapping

[ -f material-class-mapping.csv ] || wget https://raw.githubusercontent.com/MSF-Jarvis/random-bits-and-pieces/master/scripts/material-class-mapping.csv

parallel --bibtex # Praise the holy GNU
for mapping in androidx-class-mapping.csv material-class-mapping.csv; do
    for item in $(cat "${mapping}"); do
        orig=$(echo "${item}" | cut -d ',' -f 1)
        new=$(echo "${item}" | cut -d ',' -f 2)
        printf "Refactoring %s to %s\n" "${orig}" "${new}"
        find app/src/main -type f | parallel -j+1 sed -i "s#$orig#$new#g" {} \;
    done
done