try:
    f = open("file.txt","r")
except IOError as err:
    print("Terjadi kesalahan: {}".format(err))