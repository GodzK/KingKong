class Animal:
    def __init__(self, name):
        self.name = name 
    
    def sound(self):
        return "..."
    

class Dog(Animal):
    
    def __init__(self, name, color):
        super().__init__(name) 
        self.color = color       
    
    def sound(self):
        return "Bok Bok"
    
    def eat(self):
        return "snack"
    

# การสร้างออบเจกต์
dog = Dog("Bo" , "red")


print(f"Animal name: {dog.name}, Dog color: {dog.color}, Dog sound: {dog.sound()}")
