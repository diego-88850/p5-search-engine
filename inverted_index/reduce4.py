#!/usr/bin/env python3
"""Reduce 4. Takes KEY(word) VALUES(idfk (inverse freq over all doc), docIdk, tfik (freq in specific doc), |di|).
Combines the words from past round, which were separated by documents to calculate |di|.
KEY(authors)	VALUES(0.17609125905568124 44664014 1 3.6)
KEY(authors)    VALUES(0.17609125905568124 66670203 1 5.8)
->
KEY(authors)    VALUE(0.17609125905568124 44664014 1 3.6 66670203 1 5.8 )"""

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


def reduce_one_group(word, group):
    """Reduce one group."""
    finalValue = ""
    
    for line in group:
        values = re.split(" |\t|\n", line)
        idfk = values[1]
        docId = values[2]
        wordCount = values[3]
        di = values[4]
        finalValue += docId + " " + wordCount + " " + di + " "
    
    print(f"{word}\t{idfk} {finalValue.strip()}")

if __name__ == "__main__":
    main()