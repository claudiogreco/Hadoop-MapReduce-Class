#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve the popular tags problem.
=============================================================
"""

import sys
import csv
from collections import defaultdict

def reducer():
    # Reads the CSV file from the standard input.
    reader = csv.reader(sys.stdin, delimiter='\t')

    # Last key read from the standard input.
    old_key = None

    # Occurrences of each tag.
    tag_occurrence = defaultdict(int)

    # Top 10 of the tags.
    top_10 = []

    # Occurrences of the current tag.
    tag_count = 0

    for line in reader:
        # Checks if the line has been successfully parsed.
        if len(line) != 2:
            continue

        # Saves the tag.
        this_key = line[0]

        # Deals with the change of the tag.
        if old_key and old_key != this_key:
            add_tag(old_key, tag_count, top_10)
            tag_count = 0
            old_key = this_key

        # Updates the occurrences of the current tag.
        tag_count += 1

        # Updates the tag.
        old_key = this_key

    # Deals with the last element.
    if old_key != None:
        add_tag(old_key, tag_count, top_10)

    # Prints the top 10.
    print top_10

def add_tag(tag, tag_count, top_10):
    # Adds the tag to the top 10.
    top_10.append([tag, tag_count])
    
    # Sorts the tags in a descending order by their number of occurrences.
    top_10.sort(key = lambda x: x[1], reverse=True)

    # Keeps just the first 10 elements of the list.
    top_10 = top_10[:10]

if __name__ == '__main__':
    reducer()
