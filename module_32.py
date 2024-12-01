# import module31

# print(module31.sum(4,12))
#
# print((module31.mul(6,12)))

# as a alies

import module31 as num
print(num.sum(34,9))
print(num.mul(3,89))


from module31 import sum
print(sum(34,24))

from module31 import mul
print(mul(34,89))


from module31 import *

print(sum(45,78))
print(mul(2,6))

