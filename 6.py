# logicals opeators
# 1-and
# 2-or
# 3- not


a = 45
b = 45
c=54
print(a==b and c>=b )
print(a==b or a<=34)
print( not a!=b)






a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")




    a = 10
    b = 12
    c = 0
    if a and b and c:
        print("All the numbers have boolean value as True")
    else:
        print("Atleast one number has boolean value as False")



        a = 10
        if not a:
            print("Boolean value of a is True")
        if not (a % 3 == 0 or a % 5 == 0):
            print("10 is not divisible by either 3 or 5")
        else:
            print("10 is divisible by either 3 or 5")




