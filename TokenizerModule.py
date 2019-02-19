import collections
import re
import sys


class Tokenizer:

    # the init takes care of making an empty dict, opens the text file, and calls the function to tokenize such file
    def __init__(self, text_file):
        self._tokens = collections.defaultdict(int)
        self._text_file = text_file
        self._total_words_in_file = 0
        self._create_tokens()



    # tokenizes using an re expression
    # this function has a polynomial runtime O(n^2)
    def _create_tokens(self):

            list_of_tokens = re.split('[^a-zA-Z0-9]', self._text_file)

            for token in list_of_tokens:

                if token != '':
                    self._tokens[token.lower()] += 1
                    self._total_words_in_file += 1




    # prints tokens in order according to frequency first, then by alphabetical order
    # runtime complexity is O(n log n) due to the sorted method
    def print_tokens(self):

        count = 0

        for token in sorted(self._tokens.items(), key = lambda x: (-x[1], x[0]), reverse = False):
            count += 1

            if count != len(self._tokens):

                print( (token[0] + "\t" + str(self._tokens[token[0]])) )

            else:

                sys.stdout.write((token[0] + "\t" + str(self._tokens[token[0]])))

    # time complexity of O(min(n,m))
    def common_tokens(self, tokenizer_object):

        count = 0

        # checking inequality here just in case one of the objects
        # dict is much smaller. if so then itll be quicker to compare
        if len(self._tokens) < len(tokenizer_object._tokens):
            for token in self._tokens.keys():
                if token in tokenizer_object._tokens:
                    count += 1
        else:
            for token in tokenizer_object._tokens.keys():
                if token in self._tokens:
                    count += 1

        return count

    def give_dict(self):
        return self._tokens

    def give_total_terms(self):
        return self._total_words_in_file












