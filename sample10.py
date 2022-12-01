print('\n40) classes:\n')

class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()

print('\n41) modules:\n')

import dog

dog.bark()

from dog import bark

bark()

from lib import dog

dog.bark()

from lib.dog import bark

bark()

#official python libs

#math
#re for regular  expressions
#json
#datetime
#sqlite3 for SQLite
#os for Operating System utilities
#random
#statistics
#requests for HTTP requests
#http for HTTP servers
#urllib to manage URLs

import math

print(math.sqrt(4))

from math import sqrt

print(sqrt(4))

print('\n42) cli agrs:\n')

import sys

print("just type: 'py .\sample10.py beau 39' in terminal to print args")
print(sys.argv)

name = sys.argv[1]
print("Hello " + name)

import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar='color',
required=True, choices={'red', 'blue'}, help='the color to search for')

args = parser.parse_args()

print(args.color)