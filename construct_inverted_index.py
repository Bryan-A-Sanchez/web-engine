from index_loader_saver import save_index
import pathlib
from TokenizerModule import Tokenizer
from lxml import html
import json
from collections import defaultdict
from ranker import tf, idf

import datetime
currentDT1 = datetime.datetime.now()


try:
    p = pathlib.WindowsPath('.')  # gives me all the files in the current dir
    # p = [x for x in p.iterdir() if x.is_dir()][2]  # goes to the 'webpages' directory
    p = pathlib.WindowsPath('WEBPAGES_RAW')
    # url_dict_links = [x for x in p.iterdir() if not x.is_dir()][0]
    url_dict_links = pathlib.WindowsPath('WEBPAGES_RAW/bookkeeping.json')
    p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir
except NotImplementedError:
    p = pathlib.PosixPath('.')  # gives me all the files in the current dir
    # p = [x for x in p.iterdir() if x.is_dir()][2]  # goes to the 'webpages' directory
    p = pathlib.PosixPath('WEBPAGES_RAW')
    url_dict_links = pathlib.PosixPath('WEBPAGES_RAW/bookkeeping.json')
    p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir


practice_indexer = defaultdict(list)

with open(url_dict_links, 'r') as file:
    url_dict = file.read()

url_dict = json.loads(url_dict)


for sub_file in p:  # for every file in the web pages folder

    for file in sub_file.iterdir():  # go in that file and iterate through the files
        #print(file)

        with open(file, 'r', encoding='utf-8') as temp:
            # temp_readline = str(temp.readlines())
            tree = html.parse(temp)
            try:
                tree = tree.find('.//*')
            except AssertionError:
                #  if it comes in here, then that means the file wasnt an html file
                tree = None

        # tree = html.fromstring(temp_readline).find('.//*')

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

            tokenizer_object = Tokenizer(' '.join([string.text for string in strings
                                                   if string.text is not None]))

            current_file_dict = tokenizer_object.give_dict()

            doc_total = tokenizer_object.give_total_terms()

            for x in current_file_dict:
                term_freq = current_file_dict[x]

                current_tf = tf(term_freq, doc_total)
                total_num_of_corpus = 37497
                #  word_num_files = len(current_file_dict[x])

                #current_idf = idf(total_num_of_corpus, word_num_files)

                practice_indexer[x].append((current_file_dict[x],
                                            url_dict[str(file).lstrip('WEBPAGES_RAW\\').replace('\\', '/').lstrip('/')],
                                            term_freq, doc_total, total_num_of_corpus))

practice_indexer2 = defaultdict(list)
for word in practice_indexer:
    for item in practice_indexer[word]:
        practice_indexer2[word].append((tf(item[2], item[3])*idf(item[4], len(practice_indexer[word]))
                                  ,item[2]
                                  , item[1]))

    practice_indexer2[word] = sorted(practice_indexer2[word], key=lambda x: -x[0])



print('\n', len(practice_indexer))

#save_index(practice_indexer)
save_index(practice_indexer2)


if __name__ == "__main__":
    # file.print_tokens()
    currentDT = datetime.datetime.now()
    print('time start:', str(currentDT1))
    print('time finish:', str(currentDT))
