#!/usr/bin/python

"""
=============================================================
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve question 1 of problem set 1.
We are asked to answer to the following question:
'Instead of breaking the sales down by store, give us a
sales breakdown by product category across all of our stores.'
=============================================================
"""

import sys

def reducer():
    # Last key read from the standard input.
    old_key = None

    # Sales breakdown by product category.
    sales_total = 0

    # Loops around the data, which will be in the format: key\tval,
    # where key is the item, val is the sale amount.
    for line in sys.stdin:
        # Parses the current line.
        mapped_data = line.strip().split("\t")

        # Checks if the line has been successfully parsed.
        if len(mapped_data) != 2:
            continue
    
        # Saves the item and the sale amount.
        this_key, this_sale = mapped_data
    
        # Deals with the change of the item.
        if old_key and old_key != this_key:
            print old_key, "\t", sales_total
            old_key = this_key;
            sales_total = 0
    
        # Updates the item.
        old_key = this_key
    
        # Updates the sale amount.
        sales_total += float(this_sale)

    # Deals with the last element.
    if old_key != None:
        print old_key, "\t", sales_total

if __name__ == '__main__':
    reducer()
