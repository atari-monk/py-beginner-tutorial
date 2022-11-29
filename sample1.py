import random

print('\n1) vars:\n')
def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    return computer_choice

print(get_choices())
choices = get_choices()
print(choices)

def greeting():
    return "Hi"
response = greeting()
print(response)

print('\n2) dict:\n')
dict = {"name": "beau", "color": "blue"}
dict = {"name": "beau", "color": choices}
def get_dict():
    player_choice = "rock"
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
print(get_dict())

print('\n3) input:\n')
def get_input():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
get_input()

print('\n4) lists:\n')
food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)
print(food)
print(dinner)

print('\n5) random:\n')
def get_choices_final():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options);
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
print(get_choices_final())

print('\n6) args:\n')
def check_win(player, computer):
    return [player, computer]

print(check_win('player', 'computer'))

print('\n7) if:\n')
a = 3
b = 5
if a > b:
    print("yes")
if a < b:
    print("yes")
if a == b:
    print("yes")
if a != b:
    print("yes")
if a <= b:
    print("yes")
if a >= b:
    print("yes")

def check_win_if(player, computer):
    if player == computer:
        return "It's a tie!"

print(check_win_if('player', 'computer'))

print('\n8) concatenation:\n')
def check_win_con(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie!"

print(check_win_con('player', 'computer'))

print('\n9) string interpolation:\n')
age = 25
print(f"Jim is {age} years old.")

print('\n10) if else:\n')
if age >= 18:
    print("You are an adult.")
else:
    print("You are an child.")