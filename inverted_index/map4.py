#!/usr/bin/env python3
"""Map 4. Takes KEY(word) VALUES(idfk (inverse freq over all doc), docIdk, tfik (freq in specific doc), |di|).
Combines the words from past round, which were separated by documents to calculate |di|.
KEY(authors)	VALUES(0.17609125905568124 44664014 1 3.6)
KEY(authors)    VALUES(0.17609125905568124 66670203 1 5.8)
->
KEY(authors)    VALUE(0.17609125905568124 44664014 1 3.6 66670203 1 5.8 )"""
import sys
import re

for line in sys.stdin:
    print(re.sub("\n", "", line))