def lipat_ganda(x):
	return x * 3

mylist = [1,2,3]
mylistTampungan = []

# tidak pythonic
for i in mylist:
	mylistTampungan.append(lipat_ganda(i))

# pythonic
mylistTampungan = list(map(lipat_ganda, mylist))
print(mylistTampungan)