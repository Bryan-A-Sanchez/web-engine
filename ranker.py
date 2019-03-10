import math

def tf(term_freq, doc_total)-> float:
    tf_num = (1 + math.log(term_freq))

    if tf_num <= 0:
        return 0
    else:
        return tf_num

def idf(total_files, word_num_files)-> float:
    return math.log(total_files/word_num_files)


def average (my_list):
    sum = 0
    for item in my_list:
        sum+=item
    ave = sum/len(my_list)
    return ave

def variance (my_list):
    var = 0
    ave = average(my_list)
    for item in my_list:
        var += (ave-item)**2
    return var / len(my_list)