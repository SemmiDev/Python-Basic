x = '      bahasa python -> guido van rossum'

print('sebelum : ' + x)
print('sesudah : ' + x.strip())

y = x.upper()
print('uppercase : ' + y)
print('lowercase : ' + y.lower())
replacee = y.replace('->', '=>')
print(replacee)

name = '    My name is, Sammi Aldhi Yanto'
gabungan = name.strip().upper().replace(',', '->')
print(gabungan)
