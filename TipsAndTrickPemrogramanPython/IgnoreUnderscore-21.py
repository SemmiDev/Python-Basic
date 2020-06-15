listku = [1,2,3,4,5]
# awal
a,b, *_ = listku
print(a,b)

# akhir
*_,a,b = listku
print(a,b)

# dll
for _ in listku:
	print("ha")

