def bagi(x):
    if x < 0:
       raise ValueError("Haruss  positif")
    return x

x = 3
try:
    hasil = bagi(x)
    print(hasil)
except:
    print("harus positif")
finally:
    # akan selalu dijalankan : untuk beres2
    print("ini finally")


def test(someoneTest):
    if someoneTest ==  "fauziah ramadhani":
        raise ValueError("cari yang lain :(")
    else:
        return "ya, kamu kamu berhak"

if __name__ == '__main__':
    names = str(input("Masukkan nama yg engkau suka : "))
    test(names)
    # Sammidev