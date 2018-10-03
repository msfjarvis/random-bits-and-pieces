#!/usr/bin/env python3.5

import os
import re

rootDir='.'

for dirName, subdirList, fileList, in os.walk(rootDir):
    for dname in subdirList:
        normalised_dir_name = re.sub(' ', '.', re.sub(' \(.*', '', dname))
        if (dname != normalised_dir_name):
            os.rename(dirName + '/' + dname, normalised_dir_name)
