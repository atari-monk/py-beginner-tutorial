print('\n25) number data types:\n')

num1 = 2 + 3j
num2 = complex(2,3)
print(num2.real, num2.imag)

print('\n26) build in number functions:\n')

print(abs(-5.5))
print(round(5.49))
print(round(5.49, 1))

print('\n27) enums:\n')

#its only way to make constants in python

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(list(State))
print(len(State))

print('\n28) input:\n')

age = input("What is your age? ")
print("Your age is " + age)

print('\n29) control statements:\n')

condition = True

if condition == True:
    print("The condition")
    print("was true")

print("print outside if")

if condition == True:
    print("The condition")
    print("was true")
else:
    print("The condition")
    print("was false")

condition = "False"
name = "Roger"

if condition == True:
    print("The condition")
    print("was true")
elif name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio")
else:
    print("The condition")
    print("was false")

print('\n30) lists:\n')

dogs = []
print(dogs)
dogs = ["Roger", 1, "Syd", True]
print("Roger" in dogs)
print(dogs[0])
print(dogs[2])
dogs[2] = "Beau"
print(dogs[2])
print(dogs)
print(dogs[-1])
dogs = ["Roger", 1, "Syd", True, "Quincy", 7]
print(dogs[2:4])
print(dogs[3:])
print(dogs[:3])
print(len(dogs))
dogs.append("Judah")
print(dogs)
dogs.extend(["Judah", 5])
print(dogs)
dogs += ["Judah", 5]
print(dogs)
dogs.remove("Quincy")
print(dogs)
print(dogs.pop())
print(dogs)

items = ["Roger", 1, "Syd", True, "Quincy", 7]
items.insert(2, "Test")
print(items)

items[1:1] = ["Test1", "Test2"]
print(items)