#dictionary holds a key,Value pairs

dict1 = {1: 'Barbara', 2: 'Java'}
print(dict1)

#Change Value in a dictionary

dict1[1] = 'Script is fun'
print(dict1)


del dict1[1]
print(dict1)

dict1[1] = 'Python is fun'
print(dict1)

print(dict1.pop(1))
print(dict1)

dict1[1] = 'I love God'
print(dict1)
 
dict1[3] = 'Barbara is very hardworking' 
print(dict1)

#pop item function removes last element in a dictionary

print(dict1.popitem())
print(dict1)

#print all keys
print(dict1.keys())

#print all values
print(dict1.values())

#Prints all key value pairs
print(dict1.items())
