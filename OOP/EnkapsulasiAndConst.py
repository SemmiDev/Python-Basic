# __ -> private
# _  -> protected

class Person:
    __name = ""
    __umur = 0

    #constructor
    def __init__(self,name,umur):
        self.__umur = umur
        self.__name = name

    # getter
    def getUmur(self):
        return self.__umur

    # setter
    def __setUmur(self,umurBaru):
        self.__umur = umurBaru if umurBaru >= 0 else 0

p = Person("Sammi",18)
print(p.getUmur())