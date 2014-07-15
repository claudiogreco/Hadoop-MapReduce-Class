#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 3 of problem set 1.
We are asked to answer to the following question:
'What is the total number of sales and
the total sales value from all the stores?'
=============================================================
"""

import sys

def mapper():
    # Each line of the dataset presents the following format:
    # date\ttime\tstore name\titem description\tcost\tmethod of payment.
    # For each line, the mapper writes elements 3 (item) and 4 (cost)
    # to the standard output, separated by a tab character.
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print "{0}\t{1}".format(item, cost)

if __name__ == '__main__':
    mapper()
