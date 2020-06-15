class Person:  # parent class
    # constructor
    def __init__(self, name="noname", age=0):
        self.name = name
        self.__age = age

    def getName(self, ):  # getter
        return self.name

    def getAge(self):
        return self.__age

    def setName(self, name):  # setter
        self.name = name

    def setAge(self, age):
        self.__age = age

    def intro(self):  # ibarat toString kalau di Java
        return "Nama saya yaitu " + self.name + ", berumur " + str(self.__age) + " tahun"


class PersonChild(Person):  # inheritance (pewarisan dari class parent)
    def __init__(self, name="noname", age=0, id="1"):
        super().__init__(name=name, age=age)
        self.__id = id

    def intro(self):  # timpa method / attribute dari class parent -> override
        return super().intro() + "saya mempunyai id : " + self.__id

    def introChild(self):  # child tersendiri
        return "id -> " + self.__id


if __name__ == '__main__':  # main method
    people = Person("sam", 13)
    print(people.intro())

    peopleChild = PersonChild("dev", 12)
    peopleChild2 = PersonChild("dev", 12, "2")
    print(peopleChild.intro())
    print(peopleChild2.introChild())

# source => @SammiDev
