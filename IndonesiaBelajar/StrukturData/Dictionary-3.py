import json

data_siswa = {
    "id": 1,
    "name": "Sam",
    "name": "dev",  # akan ditimpa
    "hobby": ["selvie", "belajar"],
    "address": {
        "street": "Durian",
        "country": "Indonesia"
    }
}

data_siswakosong = {}

print(data_siswa)
print(data_siswa["hobby"][0])
print(data_siswa["address"]["street"])
print(data_siswa.get("name"))  # get
print(data_siswa.get("skills", "data tidak ditemukan"))  # get alternatif (mirip exceptions)

data_siswa2 = data_siswa

# ambil keys
print(data_siswa2.keys())  # keys
for kunci in data_siswa2:
    print('-> ', kunci)
print(data_siswa2.values())  # values

# items
daftar_kunci_nilai = data_siswa2.items()
print(daftar_kunci_nilai)

# for
for k, y in data_siswakosong:
    print(f'key -> {k} value -> {y}')

# ubah
data_siswa2["name"] = "sammidev"
print(data_siswa2)

# tambah key value
data_siswa2["age"] = 17
print(data_siswa2)

# update = parameter berupa dict / update banyak data
data_siswa2.update({
    "name": "dev",
    "age": 20
})

print(data_siswa2)

# hapus
data_siswa2.pop("name")  # hapus nama
print(data_siswa2)

datapop = data_siswa2.pop("name", "data tidak ditemukan")
print(datapop)

# concat dict
a = {
    "name": "sam",
    "age": 17
}

b = {
    "class": 12,
    "skills": ["programming", "photography"]
}

c = {**a, **b}
print(c)

# ubah ke json
with open('file.json', 'w') as fileku:
    json.dump(c, fileku)


# json ke dict
with open('file.json','r') as fileku:
    dictku = json.load(fileku)
    print(dictku)
