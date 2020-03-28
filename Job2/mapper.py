#!/usr/bin/env python
import sys

# TF-IDF computation: Job 2
# Mapper output: document_name  word,word_count

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip('\n')

    # We are just reordering the variables in the line
    (key, word_count) = line.split('\t', 1)
    (word, doc_name) = key.split(',', 1)

    print_value = word + "," + word_count
    print '%s\t%s' % (doc_name, print_value)