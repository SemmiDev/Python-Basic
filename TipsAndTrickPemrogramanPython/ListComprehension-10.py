myList = []
# tidak pythonic
for i in range(50):
	myList.append(i + 1)
print(myList)

# pythonic 
myList2 = [x for x in range(1,51)]
print(myList2)