print('\n52) list compressions:\n')

numbers = [1,2,3,4,5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
print(numbers_power_2)

numbers_power_2=list(map(lambda n: n**2, numbers))
print(numbers_power_2)

print('\n53) polymorphism:\n')

class Dog:
    def eat(self):
        print('Eating dog food')

class Cat:
    def eat(self):
        print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

print('\n54) operator overloading:\n')
# you can overload all operators, for example __add__ (+) __floordiv__ (//) and so on...
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
roger = Dog('Roger', 8)
syd = Dog('Syd', 7)
print(roger > syd)