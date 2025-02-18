import random #Need random to generate a random integer

def choose(): #Function for choosing rock, paper, or scissors
    while True: #You cannot escape the loop unless your text matches one of the options
        x = input('You are in a game of rock, paper, scissors. What do you throw out? ')
        match x: #Switch statement in python to break out of the loop
            case 'rock':
                return 'rock'
            case 'paper':
                return 'paper'
            case 'scissors':
                return 'scissors'

def rando(): #Function to randomly choose between rock, paper, and scissors
    x = random.randint(1, 3)
    match x: #Switch statement to return a string value associated with the number
        case 1:
            return 'rock'
        case 2:
            return 'paper'
        case 3:
            return 'scissors'
        
def verse(you, ai): #All the if statements for win/tie/lose
    if you == 'rock' and ai == 'rock':
        print('It is a tie. :( ')
    elif you == 'rock' and ai == 'paper':
        print('You lose. ')
    elif you == 'rock' and ai == 'scissors':
        print('You win! ')
    elif you == 'paper' and ai == 'rock':
        print('You win! ')
    elif you == 'paper' and ai == 'paper':
        print('It is a tie. :( ')
    elif you == 'paper' and ai == 'scissors':
        print('You lose. ')
    elif you == 'scissors' and ai == 'rock':
        print('You lose. ')
    elif you == 'scissors' and ai == 'paper':
        print('You win! ')
    else:
        print('It is a tie. :( ')

verse(choose(), rando()) #Call the functions