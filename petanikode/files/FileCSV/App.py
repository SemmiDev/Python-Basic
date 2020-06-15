import csv

def openJSVFile():
    with open('contacts.csv') as csv_file:
        csv.reader = csv.reader(csv_file, delimiter =',')
        print(csv.reader)
        for row in csv.reader:
            print(row)

def parsingToList():
    contact = []
    with open('contacts.csv') as csv_file:
        csv.reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_file:
            contact.append(row)
            labelsRemove = contact.pop(0)
            print(labelsRemove)
            print(contact)

def csvToDictionary():
    contacts = []
    with open('contacts.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)
    print("id \t firstname \t lastname \t email \t gender \t department \t company")
    print("--- " * 32)
    for data in contacts:
        print(f"{data['id']} \t {data['firstname']} \t {data['lastname']} \t {data['email']} \t {data['gender']} \t {data['department']} \t {data['company']}")

csvToDictionary()