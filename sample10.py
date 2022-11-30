print('\n40) classes:\n')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()

print('\n41) classes inheritance:\n') #2:37:45

