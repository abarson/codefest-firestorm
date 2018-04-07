#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 17:08:46 2018

@author: eligitelman
"""

from collections import Counter
import numpy as np
# import matplotlib.pyplot as plt
from watson_apis import NaturalLanguageUnderstanding  
import json

test = "By leveraging the power of IBM’s Watson, Study Buddy is a suite of tools for increasing study productivity. The main tools we provide are" 


def n_words(string):
    return len(string.split(" "))
    

def most_common(string):
    words = Counter()
    words.update(string.split())
    return words.most_common()
    
        
def n_unique_words(string):
    return len(set(string.split(" ")))


def length_dist(string):
    """
    return L, N_L
    """
    words = string.split(" ")
    unique_lengths = sorted(list(set([len(word)for word in words])))
    
    L2cts = {L: 0 for L in unique_lengths}
    
    for word in words:
        L2cts[len(word)] += 1
    
    counts = [L2cts[L] for L in unique_lengths]
    
    return unique_lengths, counts


def avg_length(string):
    words = string.split(" ")
    count = [len(word)for word in words]
    average = 0
    for i in count:
        average += i
    average = average / len(count)
    return average


def st_dev(string):
    words = string.split(" ")
    count = [len(word) for word in words]
    return np.std(count)


def length_x_freq(string):
    freqs = Counter()
    freqs.update(string.split())
    words = [w for w in freqs]
    lengths = [len(w) for w in words]
    occurrences = [freqs[w] for w in words]
    return lengths, occurrences
    
    
def length_dist_plot(string):
    l, nl = length_dist(string)
    plt.title("Word Length Distribution")
    plt.xlabel("Length")
    plt.ylabel("Count")
    plt.bar(l, nl)
    plt.savefig("len_dist_plot.png")


def length_freq_plot(string):
    l, oc = length_x_freq(string)
    plt.title("Word Length by Frequency")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.scatter(l, oc)
    plt.savefig("len_freq_plot.png")


def natural_lang_understanding(string):
    """
    the natural language understanding stats of the text
    """

    nlu = NaturalLanguageUnderstanding()
    jdump = json.loads(nlu.analyze_nl(string))
    
    kw = jdump['keywords']

    avg_sadness = 0.
    avg_joy = 0.
    avg_fear = 0.
    avg_disgust = 0.
    avg_anger = 0.
    
    most_relevant_k = None
    highest_relevance = -1.

    for k in kw:

        if k['relevance'] > highest_relevance:
            most_relevant_k = k['text']
            highest_relevance = k['relevance']

        if 'emotion' in k:
            avg_sadness += k['emotion']['sadness']
            avg_joy += k['emotion']['joy']
            avg_fear += k['emotion']['fear']
            avg_disgust += k['emotion']['disgust']
            avg_anger += k['emotion']['anger']
    
    sad_str = "Average Sadness Rating : % 0.2f" % avg_sadness / len(kw)
    joy_str = "Average Joy Rating : % 0.2f" % avg_joy / len(kw)
    disgust_str = "Average Disgust Rating : % 0.2f" % avg_disgust / len(kw)
    anger_str = "Average Anger : %0.2f" % avg_anger / len(kw)
    fear_str = "Average Fear : %0.2f" % avg_fear / len(kw)
    
    highest_relevance = 
    return avg_sadness / len(kw), avg_joy / len(kw), avg_fear / len(kw), avg_disgust / len(kw), avg_anger / len(kw), highest_relevance, most_relevant_k
           

def analytics(string):
    return n_words(string), avg_length(string), most_common(string), n_unique_words(string)


# natural_lang_understanding(test)
# length_freq_plot(test)
