print('\n35) functions:\n')

def hello():
    print("Hello!")
hello()
hello()
hello()

def hello(name):
    print("Hello " + name)
hello("Beau")
hello("Quincy")

def hello(name="my friend"):
    print("Hello " + name)
hello()

def hello(name, age):
    print("Hello " + name + " , you are " + str(age) + " years old!")
hello("Beau", 39)

def change(value):
    value = 2

val = 1
change(val)

print(val)

def change(value):
    value["name"] = "Syd"

val = {"name": "Beau"}
change(val)

print(val)

def hello(name):
    print("Hello " + name + '!')
    return name

print(hello("Beau"))

def hello(name):
    print("Hello " + name + '!')
    return

def hello(name):
    if not name:
        return
    print("Hello " + name + '!')

hello(False)
hello("Beau")

def hello(name):
    print("Hello " + name + '!')
    return name, "Beau", 8
    
print(hello("Syd"))

age = 8

def test():
    print(age)
print(age)
test()

def test():
    age2 = 8
    print(age2)
test()

print('\n36) nested functions:\n')

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()

print('\n37) closures in functions:\n')

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()

print(increment())
print(increment())
print(increment())