x = 5

x += 2
x -= 3
x *= 3
x /= 4
x %= 3
x **= 2


# operator bitwise
a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))

# Operasi AND
c = a & b
print("a & b = %s" % c)

# Operasi OR
c = a | b
print("a | b = %s" % c)

# Operasi XOR
c = a ^ b
print("a ^ b = %s" % c)

# Operasi Not
c = ~a
print("~a = %s" % c)

# Operasi shift left (tukar posisi biner)
c = a << b
print ("a << b = %s" % c)

# Operasi shift right (tukar posisi biner)
c = a >> b
print ("a >> b = %s" % c)
