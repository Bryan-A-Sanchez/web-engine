import math

def tf(term_freq, doc_total)-> float:
    return term_freq/doc_total

def idf(total_files, word_num_files)-> float:
    return math.log(total_files/word_num_files)