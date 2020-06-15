def nama_fungsi():
    print("hello ini fungsi")

def salam():
    print("hello, good morning")

def greetings(message):
    print(message)

def luat_segitiga(alas,tinggi):
    luas = (alas * tinggi) / 2
    print(luas)

def luas_persegi(sisi):
    luas = sisi * sisi # bisa ini
    luas = sisi ** 2 # bisa ini
    return luas

def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

name  = "sammi"
versi = 1.0

def variableLocal():
    name = "sam"
    versi = 2.0
    print(name,versi)

def variableGlobal():
    print(name,versi)

nama_fungsi()
salam()
greetings("hello, sam")
luat_segitiga(2,3)
print(luas_persegi(5))
print(volume_persegi(5))

variableGlobal()
variableLocal()
