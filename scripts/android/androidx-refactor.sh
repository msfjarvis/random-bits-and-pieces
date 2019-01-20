#!/usr/bin/env bash

# Copyright (C) Harsh Shandilya <msfjarvis@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

# shellcheck disable=SC1117
# SC1117: Backslash is literal in "\n". Prefer explicit escaping: "\\n".

if [ ! -f /tmp/androidx-class-mapping.csv ]; then
    wget https://developer.android.com/topic/libraries/support-library/downloads/androidx-class-mapping.csv -O /tmp/androidx-class-mapping.csv
    sed -i '1d' /tmp/androidx-class-mapping.csv # Remove the first line since it's not an actual class mapping
fi

[ -f /tmp/material-class-mapping.csv ] || wget https://raw.githubusercontent.com/MSF-Jarvis/random-bits-and-pieces/master/scripts/android/material-class-mapping.csv -O /tmp/material-class-mapping.csv

parallel --bibtex # Praise the holy GNU
for mapping in androidx-class-mapping.csv material-class-mapping.csv; do
    while read -r item; do
        orig=$(echo "${item}" | cut -d ',' -f 1)
        new=$(echo "${item}" | cut -d ',' -f 2)
        printf "Refactoring %s to %s\n" "${orig}" "${new}"
        find "${1:-app/src/main}" -type f | parallel -j+1 sed -i "s#$orig#$new#g" {} \;
    done < "/tmp/${mapping}"
done
