admin = {
    "username" : "sammidev",
    "password" : "sammidev",
    "name" : {
        "firstName" : "sammi",
        "lastName"  : "dev",
    },
    "programming" : ["java","python","go"],
    "sosmed" : {
        "facebook" : "Al Dhy",
        "instagram" : "_sammidev"
    }
}


# akses nilai yg ada di dictionary
print(admin["sosmed"]["instagram"])
print(admin["username"])
print(admin["password"])

print(admin.get("username"))

for key in admin:
    print(admin[key])

for key, val in admin.items():
    print("%s : %s" % (key, val))

# mengubah nilai item dict
admin["username"] = "sammi"
print(admin["username"])

# menghapus item dari dictionry
del admin["password"]

# hapus dengan pop
admin.pop("password")

# menghapus sekaligus
admin.clear()

# menambah item ke dictionary
admin.update({
    "secondryPassword" : "saiasukeeji"
})

# panjang dict
print("total -> ", len(admin))

# cara lain dengan menggunakan constructor
warna_buah = dict(jeruk = "orange", apel = "merah", anggur ="ungu")
print(warna_buah)



