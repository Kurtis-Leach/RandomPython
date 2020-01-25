class Dog:
    def __init__ (self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def sayHello(self):
        print("Hello my name is " + self.name)


dog1 = Dog('dog1', 'breed1', 'age1')
dog2 = Dog('dog2', 'breed2', 'age2')

dog1.sayHello()

print (dog1)
print (dog2)