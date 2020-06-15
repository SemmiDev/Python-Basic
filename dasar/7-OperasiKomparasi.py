# komparasi

x = 5
y = 10

besarDari = x > y
besarSamaDari = x >= y
kecilDari = x < y
kecilSamaDari = x <= y

samaDengan = x == y
tidakSamaDengan = x != y

print(besarDari)
print(besarSamaDari)
print(kecilDari)
print(kecilSamaDari)
print(samaDengan)
print(tidakSamaDengan)



# is sebagai komparasi object identity
a = 5
b = 5
print("lokasi di memory : ", hex(id(a)))
print("lokasi di memory : ", hex(id(b)))
hasil  = a is b #true
hasil2 = a is not b #false
print(hasil)

# kalau membandingkan dengan literal maka gunakan ==
hasil = a == 5
print(hasil)




