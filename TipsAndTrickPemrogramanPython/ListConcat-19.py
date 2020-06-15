a = [1,2,3,4,5,'sam']
b = [6,7,8,9,10,False]
# c = [None] * (len(a) + len(b))
# for i in range(len(a)):
# 	c[i] = a[i]
# for i in range(len(b)):
# 	c[1 + len(a)] = b[i]
# print(c)

# pythonic
c = a + b
print(c)