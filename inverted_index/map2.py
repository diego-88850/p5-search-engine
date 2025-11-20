#!/usr/bin/env python3
"""Map 2. Takes word doc_id and combines them."
KEY (apple, 78661573) VALUE (1) -> KEY(apple) VALUE (78661573, 1)"""
import sys
import re

for line in sys.stdin:
    values = re.split(' |\t|\n', line)
    print(f"{values[0]}\t{values[1]} {values[2]}")