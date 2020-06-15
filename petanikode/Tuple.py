# Tuple dalam Python adalah stuktur data yang digunakan untuk menyimpan sekumpulan data.
# Tupe bersifat immutable, artinya isi tuple tidak bisa kita ubah dan hapus.
# Namun, dapat kita isi dengan berbagai macam nilai dan objek.

# contoh tuple
tupleSample = (123,'a',"Sammi",True)

# tuple kosong
t = ()

# tuple dengan isi satu (singelton)
# kalau tidak ditambah tanda koma maka akan dianggap sebagai string
satu = ('Isinya',)
siji = "Isinya siji",

# akses
print(tupleSample)
# perindex
print(tupleSample[0])
print(tupleSample[1])



# memotong tuple
web = (123,'a',"Sammi",True)
print(web[1:3]) # diambil value (1 -> 2)

# panjang tuple
print(len(web))


# tuple nested
tuple1 = "aku", "cinta", "kamu"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple
print(tuple3)
print(len(tuple3))


# bisa juga diisi dengan list,dictionary,boolean
t = ([1,2,3], {'nama': 'Petanikode', 'rank': 123}, True)
print(t)


# sequence unpacking
website = ("sammidev","nopass","sammisolution","www.sammisolution.com")
username,password,names,url = website
print(username)
print(password)
print(names)
print(url)

# training
def login(username,password,secretKey):
    database = ("sammidev","sammidev",000)
    usernameBase,passwordBase,secretKeyBase = database

    if username == usernameBase and password == passwordBase and secretKey == secretKeyBase:
        return  "anda berhasil login"
    else:
        return "failed"

inputUsername = input("masukkan username ->  ")
inputPassword = input("masukkan password ->  ")
inputSecretKey = int(input("masukkan secret key -> "))
test = login(inputUsername,inputPassword,inputSecretKey)
print(test)