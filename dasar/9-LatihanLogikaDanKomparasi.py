kurangDariLebihDari = float(input("Masukkan angka kurang dari 3 atau lebih dari 10\n -> "))
isCorrect = (kurangDariLebihDari < 3) or (kurangDariLebihDari > 10)
print(isCorrect)

kurangDariLebihDariSamaDengan = float(input("Masukkan angka kurang sama dari 3 atau lebih sama dari 10\n -> "))
isCorrect = (kurangDariLebihDariSamaDengan <= 3) or (kurangDariLebihDariSamaDengan >= 10)
print(isCorrect)

rentang = float(input("Masukkan angka yang lebih dari 3 dan kecil dari 10\n -> "))
isCorrect = (rentang > 3) and (rentang < 10)
print(isCorrect)

#tugas hehehe
tugas1 = float(input("Masukkan angka yang lebih besar dari 0 dan lebih kecil dari 5\n"
                     "atau angka yang lebih besar dari 8 dan lebih kecil dari 11\n -> "))
isCorrect = (tugas1 > 0 and tugas1 < 5) or (tugas1 > 8 and tugas1 < 11)
print(isCorrect)

tugas2 = float(input("Masukkan angka yang lebih kecil dari 0 atau lebih bear dari 5\n"
                     "atau angka yang lebih besar dari 11\n -> "))
isCorrect = (tugas2 < 0) or (tugas2 > 5 and tugas2 < 8) or (tugas2 > 11)
print(isCorrect)