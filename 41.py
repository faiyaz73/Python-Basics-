# converting json to python objects
# import json
import json

d='{"cname":"python","name":"faiyaz","rate":4344343}'
s=json.loads(d)
print(s)
for a in s:
    print(a,s[a])