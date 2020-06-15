import requests, json

url = 'https://covid19.mathdro.id/api/'

def coronaWorld():
    req = requests.get(url)
    getJson = json.loads(req.text)
    semuaPasien = getJson['confirmed']['value']
    pasienDeath = getJson['deaths']['value']
    pasienSembuh = getJson['recovered']['value']
    dirawat = semuaPasien - (pasienDeath + pasienSembuh)
    print('------------- Data Pasien Corona di DUNIA -------------')
    print(f' -Terinveksi : {semuaPasien} \n -Meninggal  : {pasienDeath} \n -Sehat      : {pasienSembuh} \n -Dirawat    : {dirawat}')
def coronaId():
    req = requests.get(url + 'countries/ID')
    getJson = json.loads(req.text)
    semuaPasien = getJson['confirmed']['value']
    pasienDeath = getJson['deaths']['value']
    pasienSembuh = getJson['recovered']['value']
    dirawat = semuaPasien - (pasienDeath + pasienSembuh)
    print('------------- Data Pasien Corona di iNDONESIA -------------')
    print(f' -Terinveksi : {semuaPasien} \n -Meninggal  : {pasienDeath} \n -Sehat      : {pasienSembuh} \n -Dirawat    : {dirawat}')
    print(semuaPasien)
print('1. Data covid Dunia')
print('2. Data covid Indonesia')
input = int(input('Mau cek menu yg mana -> '))
if input == 1:
    coronaWorld()
elif input == 2:
    coronaId()
else:
    exit()