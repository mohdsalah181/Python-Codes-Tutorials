## --------------------- rock, paper, scissor Game ! ------------------------- ##

import random

options = ('rock', 'paper', 'scissor')

computer = random.choice(options)
player = None
playAgain = True

print(computer)

    
while playAgain:
    
    player = input('select rock / paper / scissor: ')
    while player not in options:
        player = input('select rock / paper / scissor: ')
    
    if player == computer :
        print('equal ! play again ...')

    elif player == 'paper' and computer == 'rock':
        print('You Win !')

    elif player == 'rock' and computer == 'scissor':
        print('You Win !')

    elif player == 'scissor' and computer == 'paper':
        print('You Win !')

    else:
        print('You Lose !!')
        
    playAgainInput = input('Do You Want to Play Again? y/n:   ').lower()
    
    if playAgainInput == 'y':
        playAgain = True
    else:
        print('Thanks for playing !')
        playAgain = False
    

