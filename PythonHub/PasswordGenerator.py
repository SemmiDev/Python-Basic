import random

s = "abcdefghijklmnopqrstuvwxyz1234/567890ABCDEFGHIJKLM/NOPQRSTUVWXYZ!@#$%^&"
passwordlen = 16
password = "".join(random.sample(s,passwordlen))
print(password)