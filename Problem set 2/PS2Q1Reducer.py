#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve question 1 of problem 2.
We are asked to answer to the following question:
'Write a MapReduce program which will display
the number of hits for each different file on the web site.'
"""

import sys

total_hits = 0
old_key = None

# Loops around the data, which will be in the format: key\tval,
# where key is the page name, val is the value 1.

for line in sys.stdin:
    mapped_data = line.strip().split("\t")

    # Checks if the string has been successfully parsed.
    if len(mapped_data) != 2:
        continue

    # Saves the page name and the value 1.
    this_key, this_count = mapped_data

    # Deals with the change of the page name.
    if old_key and old_key != this_key:
        print old_key, "\t", total_hits
        old_key = this_key;
        total_hits = 0

    # Updates the page name.
    old_key = this_key

    # Updates the total number hits.
    total_hits += int(this_count)

# Deals with the last page name and total number of hits.
if old_key != None:
    print old_key, "\t", total_hits
