# polymorphism ->  means over loading and over radding
# polymorphism means same function name ( but difference signatures) being uses for difference of types.

# es me 2 cheje hoti h over loading and over ridding

# a = [23,45,26,78,15]
# print(len(a))
# s = "welcome faiyaz ansari"
# print(len(s))

# over loadding

# class sgit:
#     def display(self,name=''):
#         print(" faiyaz ansari" + name)
# obj = sgit()
# obj.display()
# obj.display('python')


# overridding


# class A:
#     def display(self):
#         print("My name is faiyaz ansari")
# class B(A):
#     def display(self):
#         super().display()
#         print(" Sgit computer centers : ")
# obj = B()
# obj.display()




# examples



# class Area:
#     def ar(self,a=None,b = None):
#         if a!=None and b!=None:
#             print("Area of Rectange",(a*b))
#         elif a!=None:
#             print("Square",(a*a))
#         else:
#             print("Noting found value")
# obj = Area()
# obj.ar()
# obj.ar(2)
# obj.ar(4,5)


# example of overriding


class over:
    def Display(self):

        print("I m a faiyaz ansari")
class over1(over):
    def Display(self):
        super().Display()
        print("My address is a gorkhapur : ")
obj = over1()
obj.Display()


