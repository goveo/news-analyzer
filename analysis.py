import numpy as np
import matplotlib.pyplot as plt
import nltk

import filter
import pymorphy2
from nltk.corpus import stopwords
from nltk import word_tokenize,sent_tokenize

morph = pymorphy2.MorphAnalyzer()

from collections import Counter


def get_colors(n):
    colors = []
    cm = plt.cm.get_cmap('tab10', n)
    for i in np.arange(n):
        colors.append(cm(i))
    return colors


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


def get_popular_words():
    titles = filter.get_all_titles()
    titles = prepare_titles(titles)
    # titles = set_titles_in_one_list(titles)

    words = dict(Counter(titles).most_common(10))

    dict_keys = list(words.keys())
    dict_values = list(words.values())
    top_keys = len(words)

    plt.title('Найчастіші слова у новинах', fontsize=10)
    plt.bar(np.arange(top_keys), dict_values, color=get_colors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=10)
    plt.ylabel('Кількість входжень', fontsize=10)
    plt.show()
# print(dict_sort(words))

get_popular_words()