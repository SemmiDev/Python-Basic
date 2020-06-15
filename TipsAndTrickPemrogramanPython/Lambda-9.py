myList  = [1,2,3,4,5]
myList2 = [2,3,4,5,6]
yourList = list(map(lambda x: x * 2, myList))
yourList = list(map(lambda x,y : x * y, myList, myList2))
print(yourList)