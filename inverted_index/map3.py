#!/usr/bin/env python3
"""Map 3. Takes KEY(word) VALUES(idfk (inverse freq over all doc), docIdk, tfik (freq in specific doc))"
KEY(authors)	VALUES(0.17609125905568124 44664014 1 67613335 1) -> calculate normalization factor via docId as key."""
import sys
import re

for line in sys.stdin:
    values = re.split(' |\t|\n', line)
    idfk = values[1]
    word = values[0]
    for idx in range(2, len(values), 2):
        if values[idx] == '': break
        print(f"{values[idx]}\t{word} {idfk} {values[idx + 1]}")