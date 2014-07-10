#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 3 of problem 1.
We are asked to answer to the following question:
'What is the total number of sales and
the total sales value from all the stores?'
"""

import sys

# Each line presents the following format:
# date\ttime\tstore name\titem description\tcost\tmethod of payment.
# We want elements 3 (item) and 4 (cost).
# We need to write them out to standard output, separated by a tab.

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)
