hobby = []
stop = False
i = 0
while(not stop):
    newHobbies = input("input your hobby -> ")
    hobby.append(newHobbies)
    i += 1

    isNext = input("add again (y/n)? -> ")
    if isNext == "n":
        stop = True

# cetak semua hobby
print("kamu memiliki hobby {} hobi".format(len(hobby)))
for show in hobby:
    print("-> {}".format(show))
