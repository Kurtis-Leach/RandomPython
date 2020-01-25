x = lambda a: a + 2
print (x(1))

def normalFunc(n):
    return lambda a : a + n
addFour = normalFunc(4)
print (addFour(4))