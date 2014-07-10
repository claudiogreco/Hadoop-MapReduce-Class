#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve question 3 of problem 1.
We are asked to answer to the following question:
'What is the total number of sales and
the total sales value from all the stores?'
"""

import sys

sales_number = 0
sales_total = 0

# Loops around the data, which will be in the format: key\tval,
# where key is the item name, val is the sale amount.

for line in sys.stdin:
    mapped_data = line.strip().split("\t")

    # Checks if the string has been successfully parsed.
    if len(mapped_data) != 2:
        continue

    # Saves the item name and the sale amount.
    this_key, this_sale = mapped_data

    # Updates the sale number and the total sale amount.
    sales_number += 1
    sales_total += float(this_sale)

# Shows the result.
print sales_number, "\t", sales_total
