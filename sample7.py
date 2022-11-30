print('\n31) sorting lists:\n')

print('\nsort:\n')

items = ["Roger", "Syd", "Beau", "Quincy"]
items.sort()
print(items)

print('\nsort mixed:\n')

items = ["Roger", "bob", "Beau", "Quincy"]
items.sort()
print(items)

print('\nsort with lower:\n')

items = ["Roger", "bob", "Beau", "Quincy"]
items.sort(key=str.lower)
print(items)

print('\nsort copy list:\n')

items = ["Roger", "bob", "Beau", "Quincy"]
itemsCopy = items[:]
items.sort(key=str.lower)
print(items)
print(itemsCopy)

print('\nsort on new list:\n')

items = ["Roger", "bob", "Beau", "Quincy"]
print(sorted(items, key=str.lower))
print(items)

print('\n32) tuples (they are immutable):\n')

names = ('Roger', "Syd")
print(names)
print(names[0])
print(names[-1])
print(len(names))
print(names.index('Roger'))
print("Roger" in names)
print(names[0:1])
names = ('Roger', "Syd", "Beau")
print(sorted(names))
newTuple = names + ('Tina', "Quincy")
print(newTuple)

print('\33) dictionaries:\n')

dog = { 'name': 'Roger', 'age': 8 }
print(dog['name'])
dog['name'] = 'Syd'
print(dog)
print(dog.get('name'))
print(dog.get('color'))
print(dog.get('color', 'brown'))
dog = { 'name': 'Roger', 'age': 8, 'color': 'green' }
print(dog.get('color', 'brown'))
print(dog)
print(dog.pop('name'))
print(dog)
print(dog.popitem())
print(dog)
dog = { 'name': 'Roger', 'age': 8, 'color': 'green' }
print('color' in dog)
print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))
print(dog.items())
print(list(dog.items()))
print(len(dog))
dog['favorite food'] = 'Meat'
print(dog)
del dog['color']
print(dog)
dogCopy = dog.copy()
print(dogCopy)

print('\34) sets:\n')

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2
print(intersect)

set1 = {"Roger", "Syd"}
set2 = {"Luna"}

union = set1 | set2
print(union)

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

diff = set1 - set2
print(diff)

subset1 = set1 > set2
print(subset1)

subset2 = set1 < set2
print(subset2)

print(len(set1))
print(list(set1))

set1 = {"Roger", "Syd", "Roger"}
print(set1)