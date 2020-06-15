# number (int)
# gada koma nya otoomatis itu jenis int
data_integer = 1
print("data : ", data_integer, ", bertipe data : ", type(data_integer))

# decimal (float)
data_float = 1.5
print("data : ", data_float, ", bertipe data : ", type(data_float))

# string (text)
data_string = "sammidev"
print("data : ", data_string, ", bertipe data : ", type(data_string))

# boolean (biner)
data_bool = True # true / false
print("data : ", data_bool, ", bertipe data : ", type(data_bool))

# khusus
# bil complex
# i = imajiner
data_complex = complex(5, 6)  # 6 : imajiner
print("data : ", data_complex, ", bertipe data : ", type(data_complex))

# tipe data bahasa c
from ctypes import c_double
data_cdouble = c_double(10.5)  #double
print("data : ", data_cdouble, ", bertipe data : ", type(data_cdouble))
