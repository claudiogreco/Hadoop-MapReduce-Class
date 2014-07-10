#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 2 of problem 2.
We are asked to answer to the following question:
'Write a MapReduce program which determines the number of hits
to the site made by each different IP address.'
"""

import sys

# Each line presents a Common Log Format. We want the ip address and its occurrence.
# We need to write them out to standard output, separated by a tab.

for line in sys.stdin:
    data = line.split()
    if len(data) > 1:
        ipAddress = data[0]
        print "{0}\t{1}".format(ipAddress, 1)
