#!/usr/bin/env python
from __future__ import division
import sys
from math import log10

# TF-IDF computation: Job 3 (Computing the TF-IDF)
# Reducer output: word,document_name   tf-idf

# We hardcode the number of documents we have, in this case is 3
NUM_DOCUMENTS = 3

# Indexes on the line
DOC_NAME_IDX = 0 # At position 0 we have the doc name
WORD_COUNT_IDX = 1 # At position 1 we have the word count
WORDS_IN_DOC_IDX = 2 # At position 2 we have how many times does the word appear in the doc

corpus_word_count = 0
old_word = None
word_stats_dict = {}
corpus_word_count_dict = {}

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.rstrip()
    (word, val) = line.split('\t', 1)
    word_stats = val.split(',')
    count = word_stats[3]

    if old_word != word:
        if old_word:
            corpus_word_count_dict[old_word] = corpus_word_count
            corpus_word_count = 0
        old_word = word
    try:
        corpus_word_count += int(count)
        if word in word_stats_dict.keys():
            word_stats_dict[word].append(word_stats[DOC_NAME_IDX] + "," + word_stats[WORD_COUNT_IDX] + ","
                                         + word_stats[WORDS_IN_DOC_IDX])
        else:
            word_stats_dict[word] = list()
            word_stats_dict[word].append(word_stats[DOC_NAME_IDX] + "," + word_stats[WORD_COUNT_IDX] + ","
                                         + word_stats[WORDS_IN_DOC_IDX])
    except:
        continue
corpus_word_count_dict[old_word] = corpus_word_count



# Computing TF-IDF
for word in corpus_word_count_dict.keys():
    word_stats_list = word_stats_dict[word]
    for word_stats in word_stats_list:
        word_stats = word_stats.split(",")
        try :
          term_frequency = int(word_stats[WORD_COUNT_IDX])/int(word_stats[WORDS_IN_DOC_IDX])
          inverse_doc_freq = log10(NUM_DOCUMENTS / corpus_word_count_dict[word])
          tf_idf = term_frequency * inverse_doc_freq
          print_key = word + "," + word_stats[DOC_NAME_IDX]
          print "%s\t%s" % (print_key, tf_idf)
        except ZeroDivisionError as ex:
          # When there is no document that contains that word
          # Hard to get here, as we extracted the words in all documents
          print word_stats[WORDS_IN_DOC_IDX]
          print "Error", ex