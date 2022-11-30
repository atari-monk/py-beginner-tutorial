print('\n38) objects:\n')

age = 8

print(age.real)
print(age.imag)
print(age.bit_length())

items = [1,2]
items.append(3)
items.pop()
print(id(items))

print('\n39) loops:\n')

a = True
while a == True:
    print("The a is True")
    a = False

c = 0
while c < 10:
    print("The c is True")
    c += 1
print("After loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15):
    print(item)

for index, item in enumerate(items):
    print(index, item)

items = ["beau", "syd", "quincy"]
for index, item in enumerate(items):
    print(index, item)

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)

for item in items:
    if item == 2:
        break
    print(item)