a = 10
b = 3

c = a + b
print(a,'+',b,'= ',c)

c = a - b
print(a,'-',b,'= ',c)

c = a / b
print(a,'/',b,'= ',c)

c = a % b
print(a,'mod',b,'= ',c)

c = a * b
print(a, '*', b, '= ', c)

# exsponen
c = a ** b
print(a, 'exsponen', b, '= ', c)

# floor, dibagi kemudian di bulatkan kebawah
c = a // b
print(a, 'floor', b, '= ', c)

# priority operation
x = 3
y = 5
z = 6

result = (x + y) * z / 2 + 10 - 5 % 4
#  priority
      #  () , exponen **, perkalian/pembagian/modulus.floor, penjumlahan/pengurangan
print(result)