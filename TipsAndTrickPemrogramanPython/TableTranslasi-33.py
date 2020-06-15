input  = 'aku tidak suka kamu'
source = 'au'
destination = 'ii'
translation_table = str.maketrans(source,destination)
output = input.translate(translation_table)
print(output)


















# input  = 'kota padang'
# source = 'aieo'
# destination = '4130'
# tabel_translasi = str.maketrans(source,destination)
# output = input.translate(tabel_translasi)
# print(output)











# output = 'k0t4 c1r3b0n' 
# translasi = {
# 	'a' : '4',
# 	'i' : '1',
# 	'e' : '3',
# 	'o' : '0'
# }

# for x in input:
# 	val = translasi.get(x)
# 	output += val if val else x
# print(output)



