#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve the study groups problem.
=============================================================
"""

import sys
import csv

def reducer():
    # Reads the CSV file from the standard input.
    reader = csv.reader(sys.stdin, delimiter='\t')

    # Last key read from the standard input.
    old_key = None
    
    # User IDs.
    user_ids = []

    for line in reader:
        # Checks if the line has been successfully parsed.
        if len(line) != 2:
            continue

        # Saves the post ID.
        this_key = line[0]

        # Saves the user ID.
        user_id = int(line[1])

        # Deals with the change of the post ID.
        if old_key and old_key != this_key:
            print old_key, "\t", user_ids
            user_ids = []
            old_key = this_key

        # Updates the list of the user IDs.
        user_ids.append(user_id)

        # Updates the post ID.
        old_key = this_key

    # Deals with the last element.
    if old_key != None:
        print old_key, "\t", user_ids

if __name__ == '__main__':
    reducer()
