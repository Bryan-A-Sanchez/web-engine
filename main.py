# programmers: Bryan Sanchez, Hanyu Shou, Eileen Buenaflor

from index_loader_saver import load_index
from pathlib import Path
from collections import defaultdict
import pathlib
import json
from ranker import variance

# size in KB of index and how many unique words in the index
def _stats(run = False):
    if run:
        count = 0

        web_index = load_index()

        print('size of index:', Path('inverted_index').stat().st_size / 1000)

        for x in web_index:
            count += 1

        print('term count', count)

# ranks multi queries
def _multi_query_ranker(web_index, word):
    combined_query = defaultdict(list)
    results = []

    for item in word:
        for i in web_index[item]:
            combined_query[i[2]].append(i[0])

    for item in sorted(combined_query.items(), key=lambda j: (-len(j[1]), -min(j[1]), variance(j[1])))[0:20]:
        results.append(item[0])

    return results

# opens the bookkeeping json file to be used by the search in the main
def _get_url_dict():
    try:
        url_dict_links = pathlib.WindowsPath('WEBPAGES_RAW/bookkeeping.json')
    except NotImplementedError:
        url_dict_links = pathlib.PosixPath('WEBPAGES_RAW/bookkeeping.json')

    with open(url_dict_links, 'r') as file:
        read_url_dict = file.read()

    return json.loads(read_url_dict)


if __name__ == '__main__':

    url_dict = _get_url_dict()

    _stats(False)

    web_index = load_index()

    word = input('Ask me anything or type #quit to leave\n').split(' ')

    while word[0] != '#quit':
        if len(word) == 1:
            for num, x in enumerate(web_index[word[0].lower()][0:20], 1):
                print(num, url_dict[x[2]])

        else:
            docs = _multi_query_ranker(web_index, word)

            for num, x in enumerate(docs, 1):
                print(num, url_dict[x])

        word = input('Ask me anything or type #quit to leave\n').split(' ')



