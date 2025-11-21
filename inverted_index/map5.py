#!/usr/bin/env python3
"""Map 5. Changes nothing. Used for custom partition required by spec."""
import sys
import re

for line in sys.stdin:
    values = re.split(' |\t|\n', line)
    idfk = values[1]
    word = values[0]
    for idx in range(2, len(values), 3):
        if values[idx] == '': break
        print(f"{int(values[idx]) % 3}\t{word} {idfk} {values[idx]} {values[idx + 1]} {values[idx + 2]}")