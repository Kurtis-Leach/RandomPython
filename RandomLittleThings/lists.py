things = [1,'cat',3,4,5,6,'dog']

print (things)
print (things[0]) #returns 1
things.append('bird') #append bird to the end of the array
print (things[2:4]) #returns every from the 2nd index and before the 4th index
print (things[:3]) #returns everything before the 3rd index
print (things[3:]) #returns everything after the 3rd index including the 3rd index
print (things.index('dog')) #return what index it is at
things.insert(4,'banana') #inserts banana into index 4
print (things)
