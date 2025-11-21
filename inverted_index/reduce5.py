#!/usr/bin/env python3
"""Reduce 2. Gets number of docs/HTML files that contain term i.e., nk then calculates inverse frequency."""
"""After this reduce we have KEY(word) VALUES(nk, docIdx, frequency in docIdx)."""
import sys
import itertools
import re

def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def reduce_one_group(key, group):
    """Reduce one group."""
    sol = {}
    for line in group:
        values = re.split(" |\t|\n", line, maxsplit=3)
        if values[1] in sol:
            sol[values[1]] = sol[values[1]] + " " + re.sub("\n", "", values[3])
        else:
            sol[values[1]] = re.sub("\n", "", " ".join(values[1:]))

    for k in sol:
        print(sol[k])
        
if __name__ == "__main__":
    main()