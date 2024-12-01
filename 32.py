# Nested Dictionary
Course = {
    'php':{"Duration":"2 month","fees":3000},
    'java':{"Duration":"3 month","fees":4000},
    'c':{"Duration":"5 month","fees":5000}
}
# print(Course['php'])
# print(Course['php']['fees'])
# print(Course.keys())
# print(Course.values())

for k,v in Course.items():
    # print(k,v)
    print(k,v['Duration'],v['fees'])