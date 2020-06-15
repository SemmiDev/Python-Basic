# Pembuatan fungsi
# maka * kita memberikan berapapun isi parameter
def panggil(*nama):
    print("daftar orang yang dipanggil ->")
    for orang in nama:
        print(orang)

# pemanggilan fungsi
panggil("dian", "deni", "agus","gusnur")
print("\n")
panggil("dian","agus","gusnur")

# ** artinya akan membuat parameter menjadi dictionary






# membuat fungsi dengan parameter *args
def kirim_sms(*nomer):
    print(nomer)

# membuat fungsi dengan parameter **kwargs
def tulis_sms(**isi):
    print(isi)

# Pemanggilan fungsi *args
kirim_sms(123, 888, 4444)

# pemanggilan fungsi **kwargs
# disebutkan parameter name nya
tulis_sms(tujuan=123, pesan="apa kabar")

