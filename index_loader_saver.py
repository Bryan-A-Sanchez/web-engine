import pickle

# pickles the object passed in
def save_index(index):

    file_name = 'inverted_index'

    file_object = open(file_name, 'wb')

    pickle.dump(index, file_object)

    file_object.close()

# return the object that was pickled
def load_index():

    file_name = 'inverted_index'

    file_object = open(file_name, 'rb')

    return pickle.load(file_object)


