from xml.dom import minidom

docs = minidom.parse("training.xml")
def showData():
    print("roles :: ",docs.firstChild.tagName)
    firstname = docs.getElementsByTagName("username")[0].firstChild.data
    lastname = docs.getElementsByTagName("lastname")[0].firstChild.data
    address = docs.getElementsByTagName("address")[0].firstChild.data
    list_hobby = docs.getElementsByTagName("hobby")
    print("Firstname: {}\nLastname: {}\nAddress: {}\n".format(firstname, lastname, address))

    for hobby in list_hobby:
        print("=== ", hobby.getAttribute("name"))

def save():
    training_xml = open("training.xml","w")
    docs.writexml(training_xml)
    training_xml.close()

def addHobby():
    hobbyInput = str(input("masukkan hobby : "))
    new_hobby = docs.createElement("hobby")
    new_hobby.setAttribute("name", hobbyInput)
    docs.firstChild.appendChild(new_hobby)
    list_hobby = docs.getElementsByTagName("hobby")
    print("success")
    print("now, you have {} hobby => ".format(len(list_hobby)))
    for hobi in list_hobby:
        print("=== ", hobi.getAttribute("name"))
    save()

def addMajor():
    majorInput = str(input("masukkan jurusan : "))
    new_major = docs.createElement("major")
    new_major.setAttribute("name", majorInput)
    docs.firstChild.appendChild(new_major)
    list_major = docs.getElementsByTagName("major")
    print("success")
    print("now, you have {} majors => ".format(len(list_major)))
    for major in list_major:
        print("=== ", major.getAttribute("name"))

    save()

def login():
    username  = input("username =>  ")
    password  = input("password =>  ")
    secretKey = input("secretKey =>  ")

    usernameBase = docs.getElementsByTagName("username")[0].firstChild.data
    passwordBase = docs.getElementsByTagName("password")[0].firstChild.data
    sercretKeyBase = docs.getElementsByTagName("secretkey")[0].firstChild.data

    if  (username == usernameBase)  and (password == passwordBase) and (secretKey == sercretKeyBase):
            print(" [1] tampilkan data\n [2] tambah data")
            inputUser = int(input("masukkan pilihan -> "))
            if inputUser == 1:
                showData()
            elif inputUser == 2:
                print(" [1] add hobby\n [2] add major")
                inputUser2 = int(input("masukkan pilihan -> "))
                if inputUser == 1:
                    addHobby()
                elif inputUser == 2:
                    addMajor()
                else:
                    print("failed")
                    exit()
    else:
        print("failed")
        exit()
login()