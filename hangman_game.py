### hangman game ###

import random


def hangManStatus(wrong):
    
    print('Wrong Char !')
    
    if wrong == 0 :
        print('------\n'
              '     |\n'
              '     |\n'
              '     |\n'
              '-------'
              )
    
    if wrong == 1 :
        print('------\n'
              '  O  |\n'
              '     |\n'
              '     |\n'
              '-------'
              )
    
    if wrong == 2 :
        print('------\n'
              '  O  |\n'
              '  |  |\n'
              '     |\n'
              '-------'
              )
        
    if wrong == 3 :
        print('------\n'
              '  O  |\n'
              '  |\ |\n'
              '     |\n'
              '-------'
              )
    
    if wrong == 4 :
        print('------\n'
              '  O  |\n'
              ' /|\ |\n'
              '     |\n'
              '-------'
              )
    
    if wrong == 5 :
        print('------\n'
              '  O  |\n'
              ' /|\ |\n'
              '   \ |\n'
              '-------'
              )
        
    if wrong == 6 :
        print('------\n'
              '  O  |\n'
              ' /|\ |\n'
              ' / \ |\n'
              '-------'
              )


def checkUserInput(char, guessedWord):
    counter = 0
    correctPositions = []
    for c in guessedWord:
        if c == char: 
            correctPositions.append(counter)
            counter+=1
        else:
            counter+=1
    return correctPositions

    
def printDetectedChar(correctGuessedChar):
    print('the detected characters are: ')
    for x in correctGuessedChar:
        print(x,end=" ")


def winCheck(correctGuessedChar,wordToGuess):
    winFlagCounter = 0
    for x in correctGuessedChar:
        if x != '_':
            winFlagCounter+=1
    if winFlagCounter == len(wordToGuess) :
        print('\n\n\nYou Win !')
        return True    
    
##----------------------------------------------------

print('-------------- Simple Hangman Game !! -----------------')
wordsList = ['madrid', 'khartoum', 'riyadh', 'cairo', 'roma', 'london', 'doha']
    
wrong = 0       
wordToGuess = random.choice(wordsList)
correctGuessedChar = []
for i in range(len(wordToGuess)):
    correctGuessedChar.append('_')


while(True):
    
    if winCheck(correctGuessedChar, wordToGuess):
        break
    
    userChar = input('\n\nguess one char: ')
    checkResult = checkUserInput(userChar, wordToGuess)
    
    if len(checkResult) == 0 :
        wrong+=1
        hangManStatus(wrong)
        printDetectedChar(correctGuessedChar)
        if wrong == 6:
            print('\nGame Over ! You Lose ...')
            break
    else:
        for x in checkResult:
            correctGuessedChar[x] = wordToGuess[x]
        printDetectedChar(correctGuessedChar)
        
