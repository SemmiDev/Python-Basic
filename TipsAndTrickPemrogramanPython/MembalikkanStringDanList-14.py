myList  = [1,2,3,4,5,6]
myList2 =[]

# tidak pythonic
for i in range(len(myList)):
	reverse_i = len(myList) - i
	myList2.append(reverse_i)
print(myList2)

# pythonic
myList3 = myList[::-1] #starting:end:step
print(myList3)

name = "Sammidev"
print(name[::-1])