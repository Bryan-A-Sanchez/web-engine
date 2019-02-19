from index_loader_saver import save_index, load_index
from TokenizerModule import Tokenizer
from pathlib import Path




if __name__ == '__main__':

    count = 0
    count_doc = 0

    web_index = load_index()

    print('size of index:', Path('inverted_index').stat().st_size/1000)

    for x in web_index:
        count += 1
        count_doc += len(web_index[x])

    print('count',count)
    print('number of documents: ', count_doc)

    web_index = load_index()

    word = input('ASK ME ANYTHING! ONLY ONE WORD PLEASE! or type #quit to leave\n')

    while word != '#quit':
        try:
             for num, x in enumerate(web_index[word.lower()][0:20], 1):

                 print(num, x[2])

        except KeyError:
            print('That word does not exist within the system.')
        word = input('ASK ME ANYTHING! ONLY ONE WORD PLEASE! or type #quit to leave\n')

    # this main will be the user prompt, it will as the user what they want and
    # return what they want. the indexing will be done in a separate area so
    # this is NOT called to create the index, this is where the index will be loaded
    # and get queried

