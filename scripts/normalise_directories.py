#!/usr/bin/env python3.5

import os
import re

rootDir='.'

for dirName, subdirList, fileList, in os.walk(rootDir):
    for dname in subdirList:
        os.rename(dname, re.sub(' ', '.', re.sub(' \(.*', '', dname)))
