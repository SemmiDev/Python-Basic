buku = []
def show_data():
    if len(buku) <= 0:
        print("belum ada data")
    else:
        for index in range(len(buku)):
            print(index,buku[index])
def insert_data():
    buku_baru = input("judul buku : ")
    buku.append(buku_baru)
def edit_Data():
    show_data()
    index = int(input("id buku : "))
    if index > len(buku):
        print("id salah")
    else:
        judul_baru = input("judul baru : ")
        buku[index] = judul_baru
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if (indeks > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[indeks])
def show_menu():
    print("\n")
    print(" ::::::::::: MENU ::::::::::: ")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] EXIT")

    menu = int(input("Pilih Menu ->> "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_Data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("salah inputan bro")

if __name__ == "__main__":
    while(True):
        show_menu()