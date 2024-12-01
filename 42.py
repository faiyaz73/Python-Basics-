# Reading and writing json file in python

import json
file = open("dummy.json","r")
x = file.read()
finalData = json.loads(x)
for a in finalData:
 # print(a)
 print(a['name'],a['language'])
