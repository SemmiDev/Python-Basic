listku = ['sam','dev','otong']
kalimat = ''
# cara lama
for kata in listku:
	kalimat += kata + " "
print(kalimat)

# cara pythonic
# separator
kalimat2 = ' '.join(listku)
kalimat3 = ':'.join(listku)

print(kalimat2)
print(kalimat3)