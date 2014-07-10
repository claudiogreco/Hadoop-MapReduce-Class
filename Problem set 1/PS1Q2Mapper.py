#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 2 of problem 1.
We are asked to answer to the following question:
'Find the monetary value for the highest
individual sale for each separate store.'
"""

import sys

# Each line presents the following format:
# date\ttime\tstore name\titem description\tcost\tmethod of payment.
# We want elements 2 (store name) and 4 (cost).
# We need to write them out to standard output, separated by a tab.

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)
