bulan = {
    'jan' : 0,
    'feb' : 1,
    'mar' : 2,
    'apr' : 3,
    'mei' : 4,
}

for i in bulan:
    bulan[i] = input("gaji : ")

tertinggi = max(bulan['jan'],bulan['feb'],bulan['mar'])
for i in bulan:
    if bulan[i] == tertinggi:
        print(i)