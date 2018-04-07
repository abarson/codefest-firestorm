a#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:23:37 2018

@author: eligitelman & dan berenberg
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer


try:
    nltk.data.find("corpus/stopwords")

except:
    nltk.download('stopwords')

STOP_WORDS = set(stopwords.words("english"))
STEMMER = SnowballStemmer("english")


def text_summary(doc, cutoff=1.0):
    """
    summarize a document in a naive way
    
    essentially it just looks at word frequencies in relation to a sentence
    args:
        doc : a string
    """
    
    words = word_tokenize(doc)
    freqtable = dict()

    for word in words:
        word = word.lower()

        if word in STOP_WORDS:
            continue
        
        word = STEMMER.stem(word)

        if word in freqtable:
            freqtable[word] += 1

        else:
            freqtable[word] = 1
     
    sentences = sent_tokenize(mytext)
    sentence_value = dict()
    
    for sentence in sentences:
        for word_val in freqtable:
            if word_val in sentence.lower():
                if sentence[:12] in sentence_value:
                    sentence_value[sentence[:12]] += freqtable[word_val]

                else:
                    sentence_value[sentence[:12]] = freqtable[word_val]

    sum_vals = 0
    for sentence in sentence_value:
        sum_vals += sentence_value[sentence]

    average = int(sum_vals / len(sentence_value))
    
    summary = ''
    for sentence in sentences:
        if sentence[:12] in sentence_value and sentence_value[sentence[:12]] > average * 1.25:
            summary += " " + sentence

    return summary


if __name__ == "__main__":
    filename = "Week1.txt"

    mytext = open(filename, 'r').read()
    text_summary(mytext)
