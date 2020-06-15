def jumlah(a, b):
    return a + b


listku = [1, 2]
dictku = {
    'a': 20,
    'b': 40
}
# positional argument
hasil  = jumlah(*listku)

# keyword argument
# harus sesuai nama variable dalam dict dengan method
hasil2 = jumlah(**dictku)
print(hasil)
print(hasil2)
