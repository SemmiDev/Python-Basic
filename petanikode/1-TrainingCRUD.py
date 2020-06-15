stop = False
stopAdmin = False

userDatabaseUsername = ["otong", "surotong", "testUser"]
userDatabasePassword = ["otongpass", "surotongpass", "testUser"]

def dashboardAdmin():
    print("Welcome back Sam")

    while (not stopAdmin):

        userAdd = input("username -> ")
        passAdd = input("password -> ")

        userDatabaseUsername.append(userAdd)
        userDatabasePassword.append(passAdd)

        isNext = input("add again (y/n)? -> ")
        if isNext == "n":
            for i in len(userDatabaseUsername):
                print(i)
            for i in len(userDatabasePassword):
                print(i)

            stopAdmin = True


def dashboardUsers(names):
    print("Welcome back {}".format(names))

def error(variant):
    print(":: {} ::".format(variant), " => the data you enter is not correct\n\n")

def loginAdmin(username,password,secretKey):
    adminDatabase = ("sammidev", "sammidev", "000")
    usernameBase,passwordBase,secretKeyBase = adminDatabase
    if (username == usernameBase) and (password == passwordBase) and (secretKey == secretKeyBase):
        dashboardAdmin()
    else:
        error("admin")


def loginUsers(username,password):
    size = len(userDatabaseUsername)
    for i in range(size):
        if username == userDatabaseUsername[i] and password == userDatabasePassword[i]:
            dashboardUsers(userDatabaseUsername[i])

def authAdmin():
    username = input("username   -> ")
    password = input("password   -> ")
    secretKey = input("secret key -> ")
    loginAdmin(username, password, secretKey)

def authUser():
    username = input("username   -> ")
    password = input("password   -> ")
    loginUsers(username, password)


while(not stop):
    print("::: LOGIN :::")
    menu = ["1. Admin", "2. Users"]

    for i in menu:
        print(i)

    choice = int(input("please be choosen one -> "))


    if choice == 1:
        authAdmin()
        stop = True

    elif choice == 2:
        authUser()
        stop = True









