print('\n11) elif:\n')

def check_win_elif(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie!"
    elif player == 'rock' and computer == 'scissors':
        return 'Rock smashes scissors! You win!'
    elif player == 'rock' and computer == 'paper':
        return 'Paper covers Rock! You lose!'

print(check_win_elif('player', 'computer'))

print('\n12) nesting if\'s:\n')

def check_win_nesting(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie!"
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! You win!'
        else: 
            return "Paper covers Rock! You lose!"
    elif player == "paper":
        if computer == 'scissors':
            return 'Scissors cut paper! You lose!'
        else: 
            return "Paper covers Rock! You win!"
    elif player == "scissors":
        if computer == 'paper':
            return 'Scissors cuts paper! You win!'
        else: 
            return 'Rock smashes scissors! You lose!'
        
print(check_win_nesting('player', 'computer'))

print('\n13) dict value\'s:\n')

choices = {"player": "rock", "computer": "paper"}
p_choice = choices["player"]
print(p_choice)