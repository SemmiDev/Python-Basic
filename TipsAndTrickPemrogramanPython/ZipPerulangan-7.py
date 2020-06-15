nim = ['001','002','003','004']
name = ['sam','dev','otong','revan']
girl = ['cila','otong','surotong','adim']

# pythonic
for d_nim, d_name,d_girl in zip(nim,name,girl):
	print(f'{d_nim} -> {d_name} mempunyai pacar yg bernama -> {d_girl}')