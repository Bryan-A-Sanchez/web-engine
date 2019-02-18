from index_loader_saver import save_index
from pathlib import Path
import pathlib
from TokenizerModule import Tokenizer
from html.parser import HTMLParser
from lxml import html
import json
from collections import defaultdict

import datetime
currentDT = datetime.datetime.now()
print('time start:', str(currentDT))

try:
    p = pathlib.WindowsPath('.')  # gives me all the files in the current dir
    # p = [x for x in p.iterdir() if x.is_dir()][2]  # goes to the 'webpages' directory
    p = pathlib.WindowsPath('WEBPAGES_RAW')
    url_dict_links = [x for x in p.iterdir() if not x.is_dir()][0]
    p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir
except NotImplementedError:
    p = pathlib.PosixPath('.')  # gives me all the files in the current dir
    # p = [x for x in p.iterdir() if x.is_dir()][2]  # goes to the 'webpages' directory
    p = pathlib.PosixPath('WEBPAGES_RAW')
    url_dict_links = [x for x in p.iterdir() if not x.is_dir()][0]
    p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir


practice_indexer = defaultdict(list)

with open(url_dict_links, 'r') as file:
    url_dict = file.read()

url_dict = json.loads(url_dict)


for sub_file in p:  # for every file in the web pages folder

    for file in sub_file.iterdir():  # go in that file and iterate through the files
        print(file)

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

            # tokenizer_object = Tokenizer(' '.join([string.text for string in strings
            #                                        if string.text is not None]))
            tokenizer_object = Tokenizer(' '.join([string.text for string in strings
                                                   if string.text is not None]))

            current_file_dict = tokenizer_object.give_dict()

            for x in current_file_dict:
                practice_indexer[x].append((current_file_dict[x],
                                            url_dict[str(file).lstrip('WEBPAGES_RAW\\').replace('\\', '/')]))
        # temp.close()

print('\n', len(practice_indexer))

save_index(practice_indexer)


if __name__ == "__main__":
    # file.print_tokens()
    currentDT = datetime.datetime.now()
    print('time finish:', str(currentDT))
