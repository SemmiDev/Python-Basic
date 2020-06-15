from xml.dom import minidom


def main():
    # parse untuk load file xml -> memory
    # dan lakukan parsing
    doc = minidom.parse("file.xml")

    # cetak isi doc dg tag pertamanya
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    nama = doc.getElementsByTagName("nama")[0].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[0].firstChild.data
    jurusan = doc.getElementsByTagName("jurusan")[0].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")

    print("Nama: {}\nAlamat: {}\nJurusan: {}\n".format(nama, alamat, jurusan))

    # bikin element
    hobi_baru = doc.createElement("hobi")
    hobi_baru.setAttribute("name", "programming")
    doc.firstChild.appendChild(hobi_baru)
    # load again
    list_hobi = doc.getElementsByTagName("hobi")

    print("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print("-", hobi.getAttribute("name"))

    # simpan permanen ke dalam file.xml
    file_xml = open("file.xml","w")
    doc.writexml(file_xml)
    file_xml.close()

main()