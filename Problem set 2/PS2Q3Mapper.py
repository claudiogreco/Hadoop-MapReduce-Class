#!/usr/bin/python

"""
Udacity's Introduction to Hadoop and MapReduce course.
MapReduce mapper to solve question 3 of problem 2.
We are asked to answer to the following question:
'Find the most popular file on the website: that is,
the file whose path occurs most often in access_log.
Your reducer should output the file's path and
the number of times it appears in the log.'
"""

import sys
import re
from urlparse import urlparse

# Each line presents a Common Log Format. We want the file path and its occurrence.
# We need to write them out to standard output, separated by a tab.

for line in sys.stdin:
    matches = re.findall(r'\"(.+?)\"',line)

    if matches:
        request = matches[0]
        url = request.split()[1]
        parsed_url = urlparse(url)
        path = parsed_url.path
        query = parsed_url.query

        if query:
            path += "?" + query

        print "{0}\t{1}".format(path, 1)
