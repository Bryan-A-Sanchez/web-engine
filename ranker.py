import math

def tf(term_freq, doc_total)-> float:
    tf_num = (1 + math.log(term_freq))

    if tf_num <= 0:
        return 0
    else:
        return tf_num

def idf(total_files, word_num_files)-> float:
    return math.log(total_files/word_num_files)