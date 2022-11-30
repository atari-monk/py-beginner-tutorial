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

