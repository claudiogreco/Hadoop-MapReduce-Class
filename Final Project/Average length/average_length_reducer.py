#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve the average length problem.
=============================================================
"""

import sys
import csv

def reducer():
    # Reads the CSV file from the standard input.
    reader = csv.reader(sys.stdin, delimiter='\t')

    # Last key read from the standard input.
    old_key = None

    # Mean of the lengths of the posts.
    lengths_mean = 0.0

    # Counter of the lengths of the posts.
    lengths_counter = 0

    # Length of the question.
    question_length = 0

    for line in reader:
        # Checks if the line has been successfully parsed.
        if len(line) != 3:
            continue

        # Saves the post ID (or parent ID), the post type and the post length.
        this_key, this_type, this_length = line

        # Deals with the change of the post ID.
        if old_key and old_key != this_key:
            if lengths_counter != 0:
                lengths_mean /= float(lengths_counter)

        print old_key, "\t", question_length, lengths_mean

        # Resets the mean of the lengths of the posts.
        lengths_mean = 0

        # Resets the counter of the lengths of the posts.
        lengths_counter = 0

        # Updates the post ID.
        old_key = this_key

        # If the post is an answer, the reducer evaluates the mean.
        if this_type == 'A':
                lengths_mean += int(this_length)
                lengths_counter += 1

        # If the post is a question, the reducer saves its length.
        elif this_type == 'Q':
                question_length = this_length

        # Deals with the last element.
        if old_key != None:
            if lengths_counter != 0:
                lengths_mean /= float(lengths_counter)
            print old_key, "\t", question_length, lengths_mean

if __name__ == '__main__':
    reducer()
