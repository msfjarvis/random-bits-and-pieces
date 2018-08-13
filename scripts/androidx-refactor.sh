#!/bin/bash

# Copyright (C) Harsh Shandilya <msfjarvis@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

[ -f androidx-class-mapping.csv ] || wget https://developer.android.com/topic/libraries/support-library/downloads/androidx-class-mapping.csv
sed -i '1d' androidx-class-mapping.csv # Remove the first line since it's not an actual class mapping

parallel --bibtex # Praise the holy GNU
for item in $(cat androidx-class-mapping.csv); do
    orig=$(echo $item | cut -d ',' -f 1)
    new=$(echo $item | cut -d ',' -f 2)
    printf "Refactoring %s to %s\n" $orig $new
    find app/src/main -type f | parallel -j+1 sed -i "s#$orig#$new#g" {} \;
done