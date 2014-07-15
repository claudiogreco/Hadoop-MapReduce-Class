#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve the study groups problem.
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
            # Saves the post ID.
            post_id = line[0]

            # Saves the post type.
            post_type = line[5]

            # Saves the author ID.
            author_id = line[3]

            # If the post is a question, the mapper writes
            # its ID and author ID to the standard output.
            if post_type == "question":
                print("{0}\t{1}".format(post_id, author_id))

            # If the posts is an answer, the mapper writes
            # its parent ID and author ID to the standard output.
            elif post_type == "answer":
                parent_id = line[6]
                print("{0}\t{1}".format(parent_id, author_id))

if __name__ == '__main__':
    mapper()
