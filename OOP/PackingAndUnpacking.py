# return
def tambah(a, b):
    return a + b


def kali(a, b):
    return a * b


def operatormtk(a, b, operator):
    return operator(a, b)


def buatFungsiKurang():
    def kurang(a, b):
        return a - b

    return kurang


def show():
    print(operatormtk(2, 3, tambah))
    print(operatormtk(3, 4, kali))
    perngurangan = buatFungsiKurang()
    print(perngurangan(2, 3))


# packing
def coordinat(x,y):
    return x,y

if __name__ == '__main__':
    koordinat = coordinat(2,3)
    print(koordinat) # packing


# unpacking
test = a,b,c = {1,2,3}
test2 = a,b,c = {1,2,3}
print(type(test))
print(type(test2))

coordinates = [(2,3),(12,3),(4,3)]
for x,y in coordinates:
    print(f'x : {x}, y : {y}' )

