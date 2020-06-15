teks = "my name is Sammi Aldhi Yanto"
# cara umum
listku = []
kata = ''
for huruf in teks:
	if huruf != ' ':
		kata += huruf
	else:
		listku.append(kata)
		kata = ''
listku.append(kata)
print(listku)

# pythonic
teks2 = "sam,adas,dasdsa,dasda"
listku2 = teks.split()
listku3 = teks2.split(',')
print(listku2)
print(listku3)