# allowing for duplicate
# allowing include different data tipe

listKosong = []
listSama = [1,2,3,4,5,6,7,6,5,5]
listDataBeda = [1,2.2,True,"Hello World",False,[1,3,2],[1,2,["a","b","c"]]]
listDataBeda2 = ["one","two","three",[1,2,3],[4,5,[1,2,3]]]

print(f'listku -> {listKosong}')
print(f'listku dengan data kedua terakhir -> {listSama[-2]}')
print(f'listku -> {listSama}')
print(f'listku -> {listDataBeda}')
print(f'listku -> {listDataBeda[2]}')
print(f'listku -> {listDataBeda2[4][2][0]}')

# slice -> ambil rentang index
# list[startindex : lastindex yg tidak disertakan]
print(f'slicing mulai dari index 2 sampai 4 => {listSama[2:5]}')
print(f'blank parameter mulai data paling awal sampai index 7 (tidak disertakan) => {listSama[:7]}')
print(f'blank parameter mulai index 4 sampai data ahir => {listSama[4 :]}')
# parameter ketiga di slicing (optional)
print(f'mulai index 2 sampai 8 dan lompat2 sebanyak 2  => {listSama[2:8:2]}')



otherList = [1,2,3,4,2,5,5,"sam",[1,2,3],True,["huruf",["b","c","d"]]]
# ubah per index
otherList[0] = 5
print(f'berubah ->{otherList}')

# tambah nilai
otherList.append(5)
otherList.append("Tambah Akhir")
print(f'berubah ->{otherList}')

# pop, keluarkan dari suatu list
tmp = otherList.pop() # delete yg ahir
print(otherList)
print("yg dihapus -> ",tmp)

# delete suatu nilai yg pertama di temui sesuai value yg di include dalam parameter
otherList.remove(2) # value
print(otherList)

# list concatination
list1 = ["aku"]
list2 = ["cinta"]
list3 = ["kamu"]
listConcat = list1 + list2 + list3
print(listConcat)