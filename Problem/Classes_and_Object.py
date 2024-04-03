class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def bark(self):
        # return f"{self.name} say woof!"
        print(f"{self.name} say woof!")

    
dog1 = Dog("Scooby",10)
dog2 = Dog("Max",5)

# print(dog1.bark())
dog1.bark()