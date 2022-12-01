print('\n49) exceptions:\n')

#result = 2 / 0
#print(result)

try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1
print(result)

#raise Exception('An error!')

try:
    raise Exception('An error!')
except Exception as error:
    print(error)

class DogNotFoundException(Exception):
    print("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')

print('\n50) with:\n')

#standard way
filename = '/Users/flavio/test.txt'
try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

#with implicit error handling
with open(filename, 'r') as file:
    content = file.read()
    print(content)

print('\n51) pip - cli for packages (on pypi.org) (analog to nugets in net):\n')

# in terminal write: pip install requests
# pip install -U requests
# pip uninstall requests
# pip show requests