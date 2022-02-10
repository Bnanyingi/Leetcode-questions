set1 = {1,2,3,4,4,4,5,5}

#add values to the set

set1.add(6)



#union(), intersection(), difference(), symmetric_difference()


#union - prints both the combination of both sets created
set2 = {3,4,5,6,8,9,0,1}
print(set1.union(set2))

#intersection - prints the intersection between the sets 
print(set1.intersection(set2))

#difference - takes out the common values in both sets and outputs the remaining values in the first set
print(set1.difference(set2))

#symmetric difference - both sets of the elements in each sets will be given as the outputs of both sets

print(set1.symmetric_difference(set2))