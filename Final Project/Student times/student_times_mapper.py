#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve the student times problem.
=============================================================
"""

import sys
import csv

def mapper():
    # Reads the CSV file from the standard input.
    reader = csv.reader(sys.stdin, delimiter='\t')

    # Skips the header.
    reader.next()

    for line in reader:
        if len(line) == 19:
            # Saves the author ID.
            author_id = line[3]

            # Saves the date of the post.
            post_date = line[8]

            # Gets the hour from the date of the post.
            post_hour = post_date[11:13]

            # Writes the author ID and the post hour to the standard output.
            print("{0}\t{1}".format(author_id, post_hour))

if __name__ == "__main__":
    mapper()
