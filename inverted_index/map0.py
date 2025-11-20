#!/usr/bin/env python3
"""Map 0. Counts the number of documents in the input."""
import sys

for line in sys.stdin:
    print(f"{line.strip()}\t1")