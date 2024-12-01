# iterate over 2 + lists at the same time (zip function)

k = [45,34,56,78,36]
l = [56,78,90,45,45]
for a,b in zip(k,l):
    print(a,b)

f =  len(l)
for n in range(f):
    print(k[n],l[n])
