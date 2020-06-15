def average(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata

print(average(1,2,4,3,2,4,5,5,6,4,3,2,3,4,2,2))
print(average(1,2,3)) # 6 / 3 = 2
print(average(1,2,4,3,2,1))
