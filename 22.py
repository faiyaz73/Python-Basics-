# String function
# 1- lower
# 2-upper
# 3-title
# 4-capitalize
# 5-find            index number find
# 6- index
# 7-isalpha         only letter check true
# 8-isdigit         only check digit
# 9-isalnum         number and letter both are applicable but any specific symbol is not sutable

#
# e = "FAIYAZ"
# s = e.lower()
# print(s)
#
# r = "faiyaz"
# t = r.upper()
# print(t)
#
# c = "FAIYAZ ANSARI"
# r = c.title()
# print(r)
#
# t = "faiyaz ansari"
# f = t.capitalize()
# print(f)



#
# e = "faiyaz"
# # r = e.find('i')
# # print(r)
# # c = e.find('a',3)                    # 3 means starting index , not value available return is -1
#
# print(e.index('a'))                    # letter index position  not value availbale error program

#
# e = "faiyaz"
# r =e.isalpha()
# print(r)

t = "323423"
b = t.isdigit()
print(b)


c = "32342e"
m = c.isalnum()
print(m)