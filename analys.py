import numpy as np
import pandas as pd
import datetime
import os
import sys
import math
import matplotlib.pyplot as plt
import nltk

import filter
import pymorphy2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import word_tokenize,sent_tokenize

morph = pymorphy2.MorphAnalyzer()

from collections import Counter

# for title in titles:
    # print(title)

# counts = Counter(list1)
# print(counts)

def normalize_word(word):
    w = morph.parse(word)[0]
    return w.normal_form


def prepare_titles(titles):
    prepared = []
    for title in titles:
        words = word_tokenize(str.lower(title))
        normalized = [normalize_word(word) for word in words
            if word.isalpha() and word not in stopwords.words("russian")]
        if len(normalized) > 0:
            prepared.append(normalized)

    toReturn = []
    for sentence in prepared:
        toReturn += sentence
    #     toReturn = [' '.join(word for word in sentence) for sentence in prepared]


    return toReturn


print("get titles")
titles = filter.get_all_titles()
titles = prepare_titles(titles)
# titles = set_titles_in_one_list(titles)

words = Counter(titles).most_common(10)
print(words)