# set is a unorder data type
# curly braket uses
# unique number
# mutable data type


# function

# set
# add
# pop          randomly delete any value
# remove
# clear
# discard      remove data
# updata
# a = {23,45,67}

# print(a)
# for b in a:
#     print(b)

l = [22,34,56,784,25]
o = set(l)
print(o)
e = {34,566,254,634}
e.remove(34)
print(e)
e.discard(634)
print(e)
print(e.pop())
e.clear()
print(e)
e.add(60)
print(e)


s = {45,566,356}
s.update(l)
print(s)