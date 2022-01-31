list1 = [1,2,3,4,5,789,546,0,3,4]

#function that sorts list in ascending order
print(sorted(list1))

#arrange in descending order

list1.sort(reverse=True)
print(list1)

#function which finds out index(positioning) of a particular element
print(list1.index(3))

#Finding count of a particular value(occurences)
print(list1.count(4))