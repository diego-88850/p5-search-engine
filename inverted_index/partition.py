#!/usr/bin/env -S python3 -u
import sys
import re

for line in sys.stdin:
    key, _, _ = line.partition("\t")
    print(int(key))