print('\n15) vars:\n')

#; for more that one instruction in line
name = "Beau"; print(name)
age = 39

print('\n16) expressions - returns value:\n')

1+1
"Beau"

print('\n17) statements - operiation on value:\n')

#this is a comment
name = "Beau" #this is an inline comment
print(name)

#in python indentation creates blocks, like {} in others

print('\n18) data types:\n')

print(type(name))
print(type(name) == str)
print(isinstance(name, str))
age = 2
print(isinstance(age, int))
age = 2.9
print(isinstance(age, float))
age = float(2)
print(isinstance(age, float))
age = "20"
print(isinstance(age, int))
age = int("20")
print(isinstance(age, int))
number = "30"
age = int(number)
print(isinstance(age, int))
number = "test"
age = int(number)
print(isinstance(age, int))

#other types:
#complex
#bool
#list
#tuple
#range
#dict
#set

print('\n19) arithmic operators:\n')

1 + 1 #2
1 + -1 #0
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
5 // 2 #2 (floor, rounds to nearest int)

"test" + "passed"

#all arithmic operators can combine with assign operator =
age = 8
age += 8 # age = age + 8
age *= 8 # age = age * 8
print(age)

print('\n20) comparison operators:\n')

a = 1
b = 2

a == b #False
a != b #True
a > b  #False
a <= b #True

print('\n21) boolean operators:\n')

a = True
b = False

not a #False
a and b #False
a or b  #True

print(0 or 1) # 1
print(False or 'hey') # 'hey'
print('hi' or 'hey') # 'hi'
print([] or False) # 'False'
print(False or []) # '[]'

print(0 and 1) # 0
print(1 and 0) # 0
print('False' and 'hey') # 'False'
print('hi' and 'hey') # 'hey'
print([] and False) # '[]'
print(False and []) # 'False'

# & binary AND
# | binary OR
# ^ binary XOR
# ~ binary NOT
# << binary shift left operation
# >> binary shift right operation

#is
#in

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

def is_adult(age):
    return True if age > 18 else False