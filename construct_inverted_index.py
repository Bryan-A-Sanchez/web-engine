from index_loader_saver import save_index, load_index
from pathlib import Path
from TokenizerModule import Tokenizer
from html.parser import HTMLParser
from lxml import html
import json
from collections import defaultdict


p = Path('.')  # gives me all the files in the current dir
p = [x for x in p.iterdir() if x.is_dir()][2]  # goes to the 'webpages' directory
url_dict_links = [x for x in p.iterdir() if not x.is_dir()][0]
p = [x for x in p.iterdir() if x.is_dir()]  # gets all the folders contained in the webpages dir

practice_indexer = defaultdict(list)

with open(url_dict_links, 'r') as file:
    urldict = file.read()

urldict = json.loads(urldict)


# count = 0
# count_subfolder = 0

for sub_file in p:  # for every file in the webpages folder
    #print(sub_file)
    count_file = 0
    for file in sub_file.iterdir():  # go in that file and iterate through the files
        # print(str(count_subfolder) + '/' + str(count_file))
        #print(sub_file)
        #print(file)

        # if count < 40000:#just used to debug a certain file, make it equal to some # to debug that file not subfolders though
        temp = open(file, 'r', encoding='utf-8')

        temp_readline = str(temp.readlines())

        tree = html.fromstring(temp_readline).find('.//*')

        if tree is not None:  # making sure that the file is html

            strings = tree.xpath('//p')

            tokenized_string = Tokenizer(' '.join([string.text for string in strings if string.text is not None]))

            current_file_dict = tokenized_string.give_dict()

            for x in current_file_dict:
                practice_indexer[x].append((current_file_dict[x],
                                            urldict[str(file).lstrip('WEBPAGES_RAW\\').replace('\\', '/')]))
        temp.close()
        # count += 1

    #     count_file += 1
    #
    # count_subfolder += 1






print('\n', len(practice_indexer))
print('\n' , count, sep = '')

save_index(practice_indexer)








if __name__ == "__main__":
    # file.print_tokens()
    print('\ndone')
