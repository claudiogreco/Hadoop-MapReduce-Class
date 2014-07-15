#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve question 2 of problem set 1.
We are asked to answer to the following question:
'Find the monetary value for the highest
individual sale for each separate store.'
=============================================================
"""

import sys

def reducer():
    # Last key read from the standard input.
    old_key = None

    # Highest sale by store name.
    highest_sale = 0.0

    # Loops around the data, which will be in the format: key\tval,
    # where key is the store name, val is the sale amount.
    for line in sys.stdin:
        # Parses the current line.
        mapped_data = line.strip().split("\t")
    
        # Checks if the line has been successfully parsed.
        if len(mapped_data) != 2:
            continue
    
        # Saves the store name and the sale amount.
        this_key, this_sale = mapped_data
    
        # Deals with the change of the store name.
        if old_key and old_key != this_key:
            print old_key, "\t", highest_sale
            old_key = this_key;
            highest_sale = 0.0
    
        # Updates the store name.
        old_key = this_key
    
        # Updates the maximum sale amount.
        if float(this_sale) > highest_sale:
            highest_sale = float(this_sale)
    
    # Deals with the last element.
    if old_key != None:
        print old_key, "\t", highest_sale

if __name__ == '__main__':
    reducer()
