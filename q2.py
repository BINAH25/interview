class Pet:
    name = 'Luna'
    def __init__(self, name):
        self.name = name
 
    def __str__(self):
        return f'My name is {self.name}.' 
 
class Dog(Pet):
    name = 'Max'
    def __init__(self, name):
        super().__init__(name)


rex = Dog('Rex')
print(rex.name)
print(Pet.name)
print(Dog.name)


