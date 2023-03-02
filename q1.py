class Laptop:
    def __init__(self, ram=8):
        self.ram = ram
 
    def set(self, ram=4):
        self.ram += ram
        return self.ram
    
laptop = Laptop()
print(laptop.ram)
laptop.set()
print(laptop.ram)
laptop.set(8)
print(laptop.ram)