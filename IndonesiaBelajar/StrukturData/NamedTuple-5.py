from collections import namedtuple

name = ("adit", "sam", "gusnur", "dandi")
aditya, sammi, goes, dandi = name
print(aditya)

Barang = namedtuple('barang',['nama','harga','garansi'])
barang1 = Barang('mouse',500,True)
barang2 = Barang(nama="keyboard",harga=200,garansi=False)
print(barang1)
print(barang2)
print(barang2.nama)
print(barang2.harga)
print(barang2.garansi)
