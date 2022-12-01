print('\n43) lambda functions:\n')

lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2,4))

print('\n44) map(), filter(), reduce():\n')

numbers = [10,20,30]
def double(a):
    return a * 2
result = map(double, numbers)
print(list(result))

numbers = [10,20,30]
double = lambda a : a * 2 
result = map(double, numbers)
print(list(result))

numbers = [10,20,30]
result = map(lambda a : a * 2, numbers)
print(list(result))

numbers = [1,2,3,4,6]
def isEven(n):
    return n % 2 == 0
result = filter(isEven, numbers)
print(list(result))

numbers = [1,2,3,4,6]
result = filter(lambda n : n % 2 == 0, numbers)
print(list(result))

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = 0
for expense in expenses:
    sum += expense[1]
print(sum)

from functools import reduce
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)

print('\n45) recursion:\n')

#3! = 3*2*1 = 6
#4! = 4*3*2*1 = 24
#5! = 5*4*3*2*1 = 120

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

print('\n46) decorators (run code around function withput changing it(logging, test performance, caching, veriffy permission and so on, or to run same code on multiple functions)):\n')

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()