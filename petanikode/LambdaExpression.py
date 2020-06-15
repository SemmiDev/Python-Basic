def square_sum(x,y):
    return x ** 2 + y ** 2

greeting = lambda name: print("hello", name)
sapa = greeting

greeting("sam")
sapa("dev")

# kelebihan lambda bisa di direct exe
hasil = (lambda x,y : x ** 2 + y ** 2)(4,6)
print(hasil)

# map
bilangan = [10,2,8,7,5,4,3,11,0,1]
filtered_result = map (lambda x: x ** 2, bilangan)
print(list(filtered_result))

# filter
genap = lambda x : x % 2 == 0
print(list(filter(genap, range(11))))
[0,2,3,4,5,6]

