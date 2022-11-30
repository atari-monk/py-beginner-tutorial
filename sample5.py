print('\n22) strings:\n')

"Beau"
'Beau'
name = "Beau"
phrase = "Beau" + " is my name"
phrase = name + " is my name"
name += " is my name"
print(name)
age = str(39)
print("""Beau is


39


years old
""")
print("Beau".upper())
print("Beau".lower())
print("bEAu person".title())
print("Beau".islower())
print("test".isalpha()) #only chars and not empty
print("test".isalnum()) #only chars or digits and not empty
print("test".isdecimal()) #only digits and not empty
print("test".startswith("te")) #to check if string starts with specific substring
print("test".endswith("st")) #to check if string ends with specific substring
print("test".replace("es", "os")) #replace part of string
print("test me".split(" ")) #split on separator char
print("  test  ".strip()) #trim whitespaces
print("test".join("ggggg")) #to append new letters to string
print("test".find("es")) #to find possition of a substring
#they return new modified string

name = "Beau"
print(name.lower())
print(name)
print(len(name))
print("au" in name)
name = "Be\"au"
print(name)
name = 'Be"au'
print(name)
name = 'Be"\'au'
print(name)
name = 'Be\nau'
print(name)
name = 'Be\au'
print(name)
name = 'Be\\au'
print(name)

print('\n23) strings characters & slicing:\n')

name = "Beau is cool"
print(name[1])
print(name[-1])
print(name[1:3])
print(name[:3])
print(name[5:])

print('\n24) bools:\n')

done = False
if done: print("yes")
else: print("no")
done = 0
if done: print("yes")
else: print("no")
done = 10
if done: print("yes")
else: print("no")
done = -1
if done: print("yes")
else: print("no")
done = "beau"
if done: print("yes")
else: print("no")
done = ""
if done: print("yes")
else: print("no")

done = True
print(type(done) == bool)
if done: print("yes")
else: print("no")

done = "beau"
print(type(done) == bool)
if done: print("yes")
else: print("no")

a = True
b = False

ab = any([a,b])
ab = all([a,b])