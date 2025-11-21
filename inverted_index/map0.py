#!/usr/bin/env python3
"""Map 0. Counts the number of documents in the input."""
import sys

for line in sys.stdin:
    if line.strip() == "<!DOCTYPE html>":
        print(f"{line.strip()}\t1")