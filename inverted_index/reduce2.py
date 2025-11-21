#!/usr/bin/env python3
"""Reduce 2. Gets number of docs/HTML files that contain term i.e., nk then calculates inverse frequency."""
"""After this reduce we have KEY(word) VALUES(nk, docIdx, frequency in docIdx)."""
import sys
import itertools
import re
import math

def main():
    """Divide sorted lines into groups that share a key."""
    
    # get total number of documents
    with open("total_document_count.txt") as file:
        N = int(next(file).strip())
    
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(N, key, group)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def reduce_one_group(N, key, group):
    """Reduce one group."""
    totalDocCount = 0
    finalValues = ""
    
    for line in group:
        values = re.split(" |\n|\t", line)
        wordCount = values[2]
        docId = values[1]

        # this is a feature of how we set up the key/value from before
        # we did word_id + word as key so now we can add them together
        totalDocCount += 1 
        
        finalValues += docId + " " + wordCount + " "
  
    idfk = math.log10(N / totalDocCount)    
    print(f"{key}\t{idfk} {finalValues}")

if __name__ == "__main__":
    main()