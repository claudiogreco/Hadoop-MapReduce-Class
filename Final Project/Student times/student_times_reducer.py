#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve the student times problem.
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

    # Number of times a post appears in a given hour.
    hour_occurrences = defaultdict(int)

    for line in reader:
        # Checks if the line has been successfully parsed.
        if len(line) != 2:
            continue

        # Saves the author ID and the post hour.
        this_key, this_hour = line

        # Deals with the change of the author ID.
        if old_key and old_key != this_key:
            max_occurrence = max(hour_occurrences.values())
            for time in [key for key in hour_occurrences.keys()
                if hour_occurrences[key] == max_occurrence]:
                print old_key, "\t", time
            old_key = this_key
            hour_occurrences = defaultdict(int)

        # Updates the number of times a post appears in a given hour.
        hour_occurrences[this_hour] += 1

        # Updates the author ID.
        old_key = this_key

    # Deals with the last element.
    if old_key != None:
        max_occurrence = max(hour_occurrences.values())
        for time in [key for key in hour_occurrences.keys() \
            if hour_occurrences[key] == max_occurrence]:
            print old_key, "\t", time

if __name__ == "__main__":
    reducer()
