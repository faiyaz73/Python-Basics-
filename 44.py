# methods,constructor

class demo:
    a = 10
    def __init__(self):

        print("My name is faiyaz ansari")
    def showvalue(self):
        # print(self.a)
       self.c = self.a*self.a
       print(self.c)
    def showvalue1(self):
        print("welcome to faiyaz")

    def sum(self,a,b):
        print(a+b)
obj = demo()
obj.showvalue()
obj.showvalue1()
obj.sum(2,23)
