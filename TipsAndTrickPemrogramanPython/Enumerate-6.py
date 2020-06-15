nim = ['001','002','003']
name = ['Sam','Otong','Surotong']

# biasa
for i in range(len(nim)):
	print(f'{nim[i]} -- {name[i]}')

# sedikit pythonic
for i, data_nim in enumerate(nim):
	print(f'{data_nim} -- {name[i]}')
