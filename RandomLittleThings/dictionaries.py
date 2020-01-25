#Dictionaries are objects
banana = {
    'color': 'yellow',
    'taste': 'good'
}
print (banana.get('color'))
banana['age'] = '1 week'
for x in banana:
    print(x)
for x, y in banana.items():
    print(x, y)
if 'color' in banana:
    print (True)
print(len(banana))
banana.pop('color') # also {del banana['color']}
print (banana)
copyBanana = banana.copy() #also {dict(banana)}
print (copyBanana) 
del banana

