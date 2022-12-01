print('\n47) docstring:\n')

"""Dog module

This module does ... bla bla bla and provides the 
following classes:

- Dog
...
"""

def increment(n):
    """Increment a number"""
    return n + 1

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print('WOF!')

print(help(Dog))

print('\n48) annotations (tool mypy will do type checks in ide\'s):\n')

def increment(n):
    return n + 1

def increment(n: int) -> int:
    return n + 1

count = 0
count: int = 0