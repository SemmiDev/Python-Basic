# casting

data_int = 10
data_float = float(data_int)  #cast to float
data_str = str(data_float) #cast to string
data_int = int(data_float)  #cast to string

print(type(data_int))
print(type(data_float))
print(type(data_str))
print(type(data_int))




# boolean
data_int2 = 0
data_bool = bool(data_int2)
print(data_bool) #false #true : selain nol
print("bertipe : ", type(data_bool))




# float -> integer :: akan di bulatkan kebawah
data_float2 = 13.2
data_float3 = 13.9
data_intFromFloat1 = int(data_float)
data_intFromFloat2 = int(data_float3)
print(data_intFromFloat1);
print(data_intFromFloat2);




# string e boolean
# summary : string kosong ->  will false if casting to booelan
# summary : string with value ->  will true if casting to booelan

a = "true"
b = "false"
c = ""

# string yg isinya number, bisa di cast ke int
# string yg isinya teks, tidak bisa di cast ke int
ab = "23"

a = bool(a)
b = bool(b)
c = bool(c)
ab = int(ab)

print(a, b, c)
print(ab)

