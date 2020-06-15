warna = ["merah","kuning",123,True,43.2]
print(warna)
print(warna[1])

# latihan
my_friends = ["adit","dandi","gusnur","rauf","ayatullah"]
# show index 3
print("isi my friend yg ke-3 : {}".format(my_friends[3]))
# show all
print("jumlah teman : {}".format(len(my_friends)))
for friend in my_friends:
    print(friend)

# ganti nilai
my_friends[1] = "sammi"

# tambah nilai
# append(item) = akhir
# insert(index,item) = index tertentu

my_friends.append("sammidev")
my_friends.insert(1,"entahlah")

# menghapus item di list
del my_friends[2]

my_friends.remove("adit") # menghapus value adit

# memotong list
print(my_friends[1:5]) #index 1 -> 4

# operasi list
# gabung list
list_lagu = [
    "no women, cry",
    "dear god"
]

list_lap = [
    "asus",
    "lenovo"
]

semua = list_lap + list_lagu
print(semua)



# list multidimensi
list_drinks = [
    ["kopi","susu","teh"],
    ["jus a","jus b", "jus c"],
    ["es a","es b","es c"]
]

print(list_drinks[0][1])

for menu in list_drinks:
    for minuman in menu:
        print(minuman)
