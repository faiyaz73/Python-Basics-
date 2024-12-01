# string formate method
#
# The formate()method formats the specified value(s) and insert them inside the string placeholder
# The placeholder is defined uaing curly brackets () read more about the placeholders in the placeholder section below

a = " my name is  {} ansari address {}".format("faiyaz","deoria")
print(a)

s = "my name is {0} ansari address {1}".format("faiyaz","gorkhpur")
print(s)

r = "my name is {1} and {0}".format("faiyaz","uttar pradesh")
t = "my numbers is {a:>10} {b} real number ".format(a=45,b=50)
print(t)
