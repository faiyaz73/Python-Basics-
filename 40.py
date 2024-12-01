# # json in python
# json(java Script object notation)
# it is mainly used for storing and transferring data between the browser and server
# json is  text written with javascript object notation
# python too supports json with a built-in packages called json .
# import json

# json supports mainly 6 data types :
# string
# boolean
# null
# object
# array
# number

import json
d={
    'cource_name':'python',
    'fees':445545
}
f=json.dumps(d)
print(f)
print(type(f))


