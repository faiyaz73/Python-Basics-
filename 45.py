# Inheritance
# in the Inheritance role of two class

# i seen three type of inheritance
# 1 - single
# 2-multi
# 3-multiple


# sinle
class A:
    def displayA(self):
        print(" welcome to sgit computers ")
class B(A):
    def displayB(self):
        print(" welcome to faiyaz ansari")
# class C(A,B):
#     def displayC(self):
#         print("my name is khan")
obj1 = B()
# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()
print(obj1)
