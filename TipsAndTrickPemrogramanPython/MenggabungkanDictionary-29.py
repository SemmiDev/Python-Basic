data1 = {'nim' : '001', 'name' : 'sammi'}
data2 = {'age': 17, 'call' : 'dev'}
data3 = {'kota' : 'padang', 'hobby' : 'reading'}
siswa = {**data1, **data2, **data3}
print(siswa)