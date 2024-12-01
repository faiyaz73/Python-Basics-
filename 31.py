# Dictionary function
# 1 - get
# 2-keys
# 3- values
# 4-items
# 5-del (with keys)
# 6-pop (with keys)
# 7-dict (dict is a dictionary create)
# 8-update
# 9-clear


# s = {"Name":"python","Rate":33434,"Duration":"3 month"}
# e = s.get("Name")
# print(e)
# for r in s.keys():
#  print(r)
#  print()
# for c in s.values():
#  print(c)
#
# print()
# for y,z in s.items():
#     print(y,z)


w = {"name":"faiyaz","roll no":24234342,"duration":"4 month","amount":23423}
del w["name"]
print(w)
p = w.pop("roll no")
print(p)
r = dict(firstName='faiyaz',lastname='ansari',hobby='codding')
print(r)
w.update({"roll no":3232})
print(w)
w.clear()
print(w)
w['disc']='this a good'
print(w)      # new disc insert