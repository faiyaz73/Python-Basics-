# Picle module
# The pickle module implements a funndamental ,but powerful algorithm for serializing (store) and
#     deserilizing (read) a python object structure.


# storing data with pickle
#
# you can pickle objects with the following data type .
#
# 1 - booleans
# 2-integers
# 3-floats
# 4-complex numbers
# 5-(normal and unicode),strings
# 6-tuples
# 7-lists
# 8-sets
# 9-dictionaries

# dump function
# dump function  is accepts data and file  objects.
# the dumb function the serilizes the data and writes it to the file. the syntax of dump () is as following
# syntax
# dump(obj,file)

import pickle
#
a = {1:3442,2:"faiyaz","rate":4566}
# file=open("dumb.txt","wb")
# pickle.dump(a,file)
# file.close()


f=open("dumb.txt","rb")
l = pickle.load(f)
print(l)