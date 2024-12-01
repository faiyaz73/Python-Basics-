# random module function
import random

print(random.randint(1,10))             # 1 and 10 include both numbers
print(random.randrange(2,10))      # 2 include but 10 is not include
l = ["apple","banana","orange","mango"]
print(random.choice(l))

print(random.random())                        # randdom any number print  0-1

l = [23,45,87,35,98]
random.shuffle(l)                             # random number come in
print(l)

u = random.uniform(3,10)                # come in any numbers 3-10

print(u)







