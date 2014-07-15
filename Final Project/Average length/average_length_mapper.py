#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve the average length problem.
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
            # Saves the post body.
            post_body = line[4]
            
            # Saves the post type.
            post_type = line[5]

            # If the post is a question, the mapper writes
            # its ID and its length to the standard output.
            if post_type == "question":
                post_id = line[0]
                print "{0}\tQ\t{1}".format(post_id, len(post_body))

            # If the post is an answer, the mapper writes
            # its parent ID and its length to the standard output.
            elif post_type == "answer":
                parent_id = line[6]
                print "{0}\tA\t{1}".format(parent_id, len(post_body))

if __name__ == '__main__':
    mapper()
