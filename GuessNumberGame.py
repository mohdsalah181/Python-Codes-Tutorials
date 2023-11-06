import random 

tries = 10

def generateRandomNumber(start,end):
    gussedNumber = random.randint(start,end)
    return gussedNumber

def checkTheGussedNumber(playerGussed, randomNumber):
    if playerGussed == randomNumber:
        return True
    else:
        return False


while True:  
    try:
        startNumber = int(input('Enter the start number: '))
    except ValueError:
        print('Enter Number')
        continue
    
    try:
        endNumber = int(input('Enter the end number: '))
        if endNumber <= startNumber:
            print('The end number must be greater than the start number !')
            continue
    except ValueError:
        print('Enter Number')
        continue
    
    numberToGuess = generateRandomNumber(startNumber,endNumber)
    break


while True:
    try:
        playerGussing = int(input('Guess The Number: '))
        if (playerGussing < startNumber or playerGussing > endNumber):
            print('This number is out of gussed range !')
            continue
    except ValueError:
        print('please enter a number !')
        continue
    
    if tries == 0:
        print('You Lose ! Try Again !')
        break
    
    if(checkTheGussedNumber(playerGussing, numberToGuess)):
        print('You Win ! \nYour Score is: ' + str(tries))
        break
        
    else:
        print('Wrong Number ! Guess Another Number')
        tries-=1
        if playerGussing > numberToGuess:
            print('Guess lesser number !')
        else:
            print('Guess greater number !')
            
    
