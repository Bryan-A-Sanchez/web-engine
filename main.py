from index_loader_saver import save_index, load_index
from TokenizerModule import Tokenizer
import sys


if __name__ == '__main__':
    web_index = load_index()

    print('size:', sys.getsizeof(web_index))

    word = input('ASK ME ANYTHING! ONLY ONE WORD PLEASE! or type #quit to leave\n')

    while word != '#quit':
        try:
            print('There are this many results for that word:', web_index[word.lower()])
        except KeyError:
            print('That word does not exist within the system.')
        word = input('ASK ME ANYTHING! ONLY ONE WORD PLEASE! or type #quit to leave\n')

    # this main will be the user prompt, it will as the user what they want and
    # return what they want. the indexing will be done in a separate area so
    # this is NOT called to create the index, this is where the index will be loaded
    # and get queried

