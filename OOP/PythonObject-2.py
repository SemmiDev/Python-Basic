class Person:
    name = "Sam"
    def copy(self):
        manusiaBaru = Person()
        a = manusiaBaru.name = "dev"
        return a

def showName():
    person = Person()
    name = "others"
    get = person.name = name
    print(get)
    print(person.copy())

showName()