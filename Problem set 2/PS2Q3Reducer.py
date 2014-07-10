#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce reducer to solve question 3 of problem 2.
We are asked to answer to the following question:
'Find the most popular file on the website: that is,
the file whose path occurs most often in access_log.
Your reducer should output the file's path and
the number of times it appears in the log.'
"""

import sys

total_hits = 0
maximum_hits = 0
most_popular_file = None
old_key = None

# Loops around the data, which will be in the format: key\tval,
# where key is the file path, val is the value 1.

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
  
    # Checks if the string has been successfully parsed.
    if len(mapped_data) != 2:
        continue
  
    # Saves the file path and the value 1.
    this_key, this_count = mapped_data
  
    # Deals with the change of the file path.
    if old_key and old_key != this_key:
        if total_hits > maximum_hits:
            maximum_hits = total_hits
            most_popular_file = old_key
        old_key = this_key;
        total_hits = 0

    # Updates the file path.
    old_key = this_key

    # Updates the total number of hits.
    total_hits += int(this_count)

# Prints the most popular file path and its total number of hits.
print most_popular_file, "\t", maximum_hits
