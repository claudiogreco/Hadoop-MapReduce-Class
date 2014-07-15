#!/usr/bin/python

"""
=========================================================
Udacity's Introduction to Hadoop and MapReduce course.
Example of implementation of a MapReduce mapper.
=========================================================
"""

import sys

def mapper():
    # Each line of the dataset presents the following format:
    # date\ttime\tstore name\titem description\tcost\tmethod of payment.
    # For each line, the mapper writes elements 2 (store name) and 4 (cost)
    # to the standard output, separated by a tab character.
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print "{0}\t{1}".format(store, cost)

if __name__ == '__main__':
    mapper()
