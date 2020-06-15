def tambah(x,y):
	return x + y
def kurang(x,y):
	return x - y

x,y = 20,10
kondisi = False
# if kondisi:
# 	hasil = tambah(x,y)
# else:
# 	hasil = kurang(x,y)
# print(hasil) 


# pythonic
hasil = (tambah if kondisi else kurang)(x,y)
print(hasil)