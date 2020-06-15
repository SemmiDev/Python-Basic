class Person:
    __name = ""
    __age = 0

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

    def __init__(self,name = "no name", age = 0):
        self.__name = name
        self.__age = age

    def introduction(self):
        return "name :", self.__name, "age : ", str(self.__age)

    # overloading
    def __add__(self, other):
        a = Person(self.getName() + other.getName(), self.getAge() + other.getAge())
        return a
    # contoh overloading yg lain ada banyak di google check aja :)

if __name__ == '__main__':
    p = Person("Sam",19)
    p2 = Person("Dev",18)
    a = p + p2
    print(a.introduction())