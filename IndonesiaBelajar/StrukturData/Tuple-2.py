# pakai tanda kurung
# perbedaan mendasar = immutable list (tidak bisa dirubah)
tupelku = (1, 2, 3, 4, 5, 5)
# tanpa tanda kurung
tupelmu = 20, 30, 40
# tupel isi satu (pakai tanda koma)
tupelku2 = 1,
# variate
tupelku3 = (True, 1, 2.0, [1, 2], (1, 2, 3), "hello", tupelku)

print(f' -> {tupelku}')
print(f' -> {tupelmu}')
print(f' -> {tupelku2}')
print(f' -> {tupelku3}')
print(f' index 0 => {tupelku3[0]}')
print(f' index 3 terakhir => {tupelku3[-3]}')
print(f'slicing => {tupelku[:4]}')
print(f'slicing => {tupelku[2:]}')
print(f'slicing => {tupelku[:5:2]}')

tupelJoin = tupelku + tupelmu
print(f'join => {tupelJoin}')

