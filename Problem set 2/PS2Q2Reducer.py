#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve question 2 of problem set 2.
We are asked to answer to the following question:
'Write a MapReduce program which determines the number of hits
to the site made by each different IP address.'
=============================================================
"""

import sys

def reducer():
    # Last key read from the standard input.
    old_key = None

    # Number of hits by ip address.
    total_hits = 0

    # Loops around the data, which will be in the format: key\tval,
    # where key is the ip address, val is the value 1.
    for line in sys.stdin:
        # Parses the current line.
        mapped_data = line.strip().split("\t")
    
        # Checks if the line has been successfully parsed.
        if len(mapped_data) != 2:
            continue
    
        # Saves the ip address and the value 1.
        this_key, this_count = mapped_data
    
        # Deals with the change of the ip address.
        if old_key and old_key != this_key:
            print old_key, "\t", total_hits
            old_key = this_key;
            total_hits = 0
    
        # Updates the ip address.
        old_key = this_key
    
        # Updates the number of hits.
        total_hits += int(this_count)
    
    # Deals with the last element.
    if old_key != None:
        print old_key, "\t", total_hits

if __name__ == '__main__':
    reducer()
