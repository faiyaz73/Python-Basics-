# Encapsulation (getter and setter)

class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,fname):
        self.__name=fname

obj = Student()
obj.setname("faiyaz")
name = obj.getname()
print(name)