jawab = 'y'
hitung = 0

while(jawab == 'y'):
    hitung += 1
    jawab = input("ulang atau tidak (y/n) -> ")

print("total perulangan : ", hitung)


hitung = 0
while(True):
    hitung += 1
    jawab = input("ulang atau tidak (y/n) -> ")
    if jawab == "n":
        break

print("total perulangan : ", hitung)