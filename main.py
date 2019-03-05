from index_loader_saver import load_index
from pathlib import Path
from collections import defaultdict

def _stats(run = False):
    if run:
        count = 0

        web_index = load_index()

        print('size of index:', Path('inverted_index').stat().st_size / 1000)

        for x in web_index:
            count += 1

        print('term count', count)


def _union(web_index, word):
    combined_query = defaultdict(float)
    for item in word:
        for i in web_index[item]:
            combined_query[i[2]] += i[0]
    return combined_query


if __name__ == '__main__':
    _stats()
    web_index = load_index()

    word = input('Ask me anything or type #quit to leave\n').split(' ')

    while word[0] != '#quit':
        if len(word) == 1:
            for num, x in enumerate(web_index[word[0].lower()][0:10], 1):
                print(num, x[2], 'score', x[0])

        else:
            union_query = _union(web_index, word)

            for num, x in enumerate(sorted(union_query.items(), key=lambda x: -x[1])[0:10], 1):
                print(num, x[0], 'score', x[1])

        word = input('Ask me anything or type #quit to leave\n').split(' ')



