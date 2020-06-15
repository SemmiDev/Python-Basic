# no duplicate
# no index
# mutable, bisa crud

setku = {1, 2, 2, "sammidev", True}
setmu = set([10, 20, 30, 40, 50])
set_kosong = set()

print(setku)
print(set_kosong)
print(setmu)

# add
setku.add("sammidev")
setku.remove(1)  # akan error jika data tidak ada (remove)
setku.discard(2)  # tidak akan erro jika data tidak ada (discard)
# ==============================================================
set1 = {1, 2, 3, 4, 0}
set2 = {3, 4, 5, 6, 0}
set3 = {5, 6, 7, 8, 0}

# gabungn / union
setunion = set1.union(set2)
setunion2 = setunion.union(set3)
setunion3 = set1.union(set2, set3)
print(setunion)
print(setunion2)
print(setunion3)

# irisan / intersection => menghasilkan set baru / irisan
intersection = set1.intersection(set2)
intersection2 = set1.intersection(set2, set3)
print(intersection)  # value yg sama
print(intersection2)  # value yg sama

# selisih / difference => set yg tidak ditemui dis et lainnya
difference = set1.difference(set2)
difference2 = set2.difference(set1)
difference3 = set2.difference(set1,set3)

print(difference)  # 1,2
print(difference2)  # 5,6
print(difference3)  # ()

# simetrik difference => ambil yg beda di dua sets / beda setangkup
simetrix = set1.symmetric_difference(set2)
print(simetrix)
