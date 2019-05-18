import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import nltk
import collections
from collections import defaultdict

import filter
import pymorphy2
from nltk.corpus import stopwords
from nltk import word_tokenize,sent_tokenize

morph = pymorphy2.MorphAnalyzer()
from collections import Counter

weekdays_list = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]

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
    titles_count = len(titles)
    titles = prepare_titles(titles)
    # titles = set_titles_in_one_list(titles)

    words = dict(Counter(titles).most_common(10))

    dict_keys = list(words.keys())
    dict_values = list(words.values())
    top_keys = len(words)

    plt.title('Найчастіші слова у новинах (оброблено {} новин)'.format(titles_count), fontsize=10)
    plt.bar(np.arange(top_keys), dict_values, color=get_colors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Кількість входжень', fontsize=10)
    plt.show()


def sort_dates_by_time(dates):
    result = defaultdict(int)
    current_day = -1
    prev_day = current_day
    days_number = -1
    for obj in dates:
        current_day = obj["date"].weekday()
        hour = obj["date"].hour
        # print(hour)
        index = hour//2
        result[index] = result[index] + 1

        if (current_day != prev_day):
            days_number += 1
        prev_day = current_day

    print(result)
    result = collections.OrderedDict(sorted(result.items()))

    for key, value in result.items():
        result[key] = value/days_number

    return (days_number, dict(result))


def get_time():
    dates = filter.get_dates()

    days_number, dates = sort_dates_by_time(dates)
    dict_values = list(dates.values())
    dict_keys = list(map(lambda x : "{}-{}".format(x*2, x*2+2), dates))
    top_keys = len(dates)

    plt.title('Кількість новин у проміжок годин дня (статистика за {} день)'.format(days_number), fontsize=10)
    plt.bar(np.arange(top_keys), dict_values, color=get_colors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Кількість новин', fontsize=10)

    plt.show()


def sort_dates_by_weekday(dates):
    result = defaultdict(int)
    for obj in dates:
        weekday = obj["date"].weekday()
        result[weekday] = result[weekday] + 1
    od = collections.OrderedDict(sorted(result.items()))
    return dict(od)


def get_weekdays():
    dates = filter.get_dates()
    dates = sort_dates_by_weekday(dates)
    print(dates)

    dict_values = list(dates.values())
    dict_keys = list(map(lambda x: "{}".format(weekdays_list[x]), dates))
    top_keys = len(dates)

    plt.title('Кількість новин у дні тижня', fontsize=10)
    plt.bar(np.arange(top_keys), dict_values, color=get_colors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Кількість новин', fontsize=10)
    plt.show()


# get_popular_words()
# get_time()
# get_weekdays()