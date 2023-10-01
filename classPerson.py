class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}"
    
    @classmethod
    def Read(cls):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        return cls(name, age)

p1 = Person.Read()
print(p1)
