from abc import ABCMeta, abstractmethod


class BangunDatar(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        "return luas bangun datar"

    # concrete method
    def __str__(self):
        return "luas => " + str(self.luas())


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.__alas, self.__tinggi = alas, tinggi

    def luas(self):
        return 0.5 * self.__alas * self.__tinggi


if __name__ == '__main__':
    s = Segitiga(2, 3)
    print(s.luas())
    print(str(s))
