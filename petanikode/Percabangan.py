user = input("anda lulus (iya/tidak)\n -> ")
if user == "iya":
    print("anda lulus")
else:
    print("anda tidak lulus")



# cases
totalBelanja = float(input("Masukkan total pembelian anda : "))
if totalBelanja > 10.000:
    print("=> total belanja kamu : ", totalBelanja)
    print("=> anda dapat diskon 50%\n")
    diskon = totalBelanja * (50 / 100)
    print("::: total :::")
    print("biaya -> ",totalBelanja - diskon)

else:
    print("biaya yg harus anda bayar : ",totalBelanja)


# elif

#file grade_nilai.py
nilai = input("Inputkan nilaimu: ")

if nilai >= 90:
   grade = "A"
elif nilai >= 80:
   grade = "B+"
elif nilai >= 70:
   grade = "B"
elif nilai >= 60:
   grade = "C+"
elif nilai >= 50:
   grade = "C"
elif nilai >= 40:
   grade = "D"
else:
   grade = "E"

print("Grade: %s" % grade)