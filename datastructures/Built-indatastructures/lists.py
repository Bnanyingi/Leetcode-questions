list2 = [1, 2, 3, 'Hello']


#add data elements to your list
#append(), extend() and insert() - add data elements to your list

list2.append((33, 9))


list2.extend((2,0))
list2.insert(3, 'Barbara')


#remove data elements to your list 
#del, pop(), remove()
del list2[3]

#pop returns the detail that has been deleted 
a = list2.pop(4)


list2.remove(2)
print(list2)

print(list2[0:2])
#Skipping an element with number of steps,normally add after specifying the elements
print(list2[0:4:2])

#Print in the reverse order
print(list2[::-1])