#!/usr/bin/env python3
"""Reduce 3. Calculates normalization factor and puts it all together."""
import sys
import itertools
import re
import math

def main():
    """Divide sorted lines into groups that share a key."""
    
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def reduce_one_group(docId, group):
    """Reduce one group."""
    di = 0
    copy = []
    
    for line in group:
        values = re.split(" ", line)
        idfk = float(values[1])
        wordCount = float(values[2])
        di += (idfk * wordCount) * (idfk * wordCount)
        copy.append(line)
    
    di = math.sqrt(di)
       
    for line in copy:
        values = re.split(" |\n|\t", line)
        word = values[1]
        idfk = values[2]
        wordCount = values[3]
        print(f"{word}\t{idfk} {docId} {wordCount} {di}")

if __name__ == "__main__":
    main()