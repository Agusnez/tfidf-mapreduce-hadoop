#!/usr/bin/env python
from string import punctuation
import sys
import os

# TF-IDF computation: Job 1
# Mapper output: word,document_name   1

# input comes from STDIN (standard input)
for line in sys.stdin:
    # Hadoop has this environment variable set
    # Allows to retrieve the name of the file
    filename = os.environ['mapreduce_map_input_file']

    # remove punctuation symbols, leading and trailing whitespaces
    line = line.translate(None, punctuation).strip('\t')
    line = line.strip()

    # split the line into words
    words = line.split()

    # increase counters
    for word in words:
        word=word.lower();
        z=word+','+filename;
        print '%s\t%s' % (z, 1)
        