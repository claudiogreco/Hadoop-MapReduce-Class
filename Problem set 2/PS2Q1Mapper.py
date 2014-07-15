#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 1 of problem set 2.
We are asked to answer to the following question:
'Write a MapReduce program which will display
the number of hits for each different file on the web site.'
=============================================================
"""

import sys
import re

def mapper():
    # Each line presents a Common Log Format (NCSA Common Log Format).
    # For each line, the mapper writes the page name and its occurrence
    # to the standard output, separated by a tab character.
    for line in sys.stdin:
        matches = re.findall(r'\"(.+?)\"',line)
        if matches:
            request = matches[0]
            url = request.split()[1]
            print "{0}\t{1}".format(name, 1)

if __name__ == '__main__':
    mapper()
