#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 2 of problem set 2.
We are asked to answer to the following question:
'Write a MapReduce program which determines the number of hits
to the site made by each different IP address.'
=============================================================
"""

import sys

def mapper():
    # Each line presents a Common Log Format (NCSA Common Log Format).
    # For each line, the mapper writes the ip address and its occurrence
    # to the standard output, separated by a tab character.
    for line in sys.stdin:
        data = line.split()
        if len(data) > 1:
            ipAddress = data[0]
            print "{0}\t{1}".format(ipAddress, 1)

if __name__ == '__main__':
    mapper()
