# Menggunakan with dan as
# Pada contoh-contoh di atas, kita selalu menutup file dengan method close().
#
# Sebenarnya file bisa ditutup otomatis dengan mengguakan with.
#
# Contoh:

with open("dokumen.txt", "r") as dok:
    print(dok.read())