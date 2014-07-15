#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve the popular tags problem.
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
            # Saves the post type.
            post_type = line[5]

            # If the post is a question, the mapper writes each
            # post tag and each occurrence to the standard output.
            if post_type == "question":
                tags = line[2].split()
                for tag in tags:
                    print "{0}\t{1}".format(tag, 1)

if __name__ == '__main__':
    mapper()
