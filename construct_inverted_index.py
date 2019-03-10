from index_loader_saver import save_index
import pathlib
from TokenizerModule import Tokenizer
from lxml import html
from collections import defaultdict
from ranker import tf, idf

import datetime
currentDT1 = datetime.datetime.now()


try:
    p = pathlib.WindowsPath('.')  # gives me all the files in the current dir
    p = pathlib.WindowsPath('WEBPAGES_RAW')
    p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir
except NotImplementedError:
    p = pathlib.PosixPath('.')  # gives me all the files in the current dir
    p = pathlib.PosixPath('WEBPAGES_RAW')
    p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir


inverted_index = defaultdict(list)

for sub_file in p:  # for every file in the web pages folder

    for file in sub_file.iterdir():  # go in that file and iterate through the files

        with open(file, 'r', encoding='utf-8') as temp:
            tree = html.parse(temp)
            try:
                tree = tree.find('.//*')
            except AssertionError:
                #  if it comes in here, then that means the file wasnt an html file
                tree = None

        if tree is not None:  # making sure that the file is html

            strings = tree.xpath('//body')
            strings.extend(tree.xpath('//title'))
            strings.extend(tree.xpath('//h1'))
            strings.extend(tree.xpath('//h2'))
            strings.extend(tree.xpath('//h3'))
            strings.extend(tree.xpath('//b'))
            strings.extend(tree.xpath('//strong'))
            strings.extend(tree.xpath('//p'))
            strings.extend(tree.xpath('//a'))
            strings.extend(tree.xpath('//address'))
            strings.extend(tree.xpath('//i'))
            strings.extend(tree.xpath('//span'))

            tokenizer_object = Tokenizer(' '.join([string.text for string in strings
                                                   if string.text is not None]))

            current_file_dict = tokenizer_object.give_dict()

            doc_total = tokenizer_object.give_total_terms()

            for x in current_file_dict:
                term_freq = current_file_dict[x]

                total_num_of_corpus = 37497

                inverted_index[x].append((current_file_dict[x],
                                          str(file).lstrip('WEBPAGES_RAW\\').replace('\\', '/').lstrip('/'),
                                          term_freq, doc_total, total_num_of_corpus))

for word in inverted_index:
    word_new_info = []
    for item in inverted_index[word]:
        #  indexer template:     word:[ (tfidf, frequency in doc, doc/url), . . .]
        word_new_info.append((tf(item[2], item[3]) * idf(item[4], len(inverted_index[word])),
                                     item[2],
                                     item[1]))

    inverted_index[word] = sorted(word_new_info, key=lambda x: -x[0])

save_index(inverted_index)


if __name__ == "__main__":
    currentDT = datetime.datetime.now()
    print('time start:', str(currentDT1))
    print('time finish:', str(currentDT))
