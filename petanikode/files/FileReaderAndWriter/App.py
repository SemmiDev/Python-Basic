puisi = open("Puisi.txt","r")
read_method1 = puisi.readlines() # read and return list
read_method2 = puisi.read() # read and return string
for text in read_method1:
    print(text)
puisi.close()

# # write files
# name = input("Name -> ")
# age  = input("Age  -> ")
# address = input("address -> ")
# # format
# teks = "Name => {}\nAge => {}\nAddress => {}".format(name,age,address)
# teks2 = ["sapi","udang","Sapi","kerbau"]
# # open
# file_bio = open("biodata.txt","w")
# file_bio2 = open("biodata2.txt","w")
# # write
# file_bio.write(teks) # all str
# file_bio.writelines(teks2) # list
# file_bio2.close()
# file_bio.close()
