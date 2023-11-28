# python code to generate a password
# -----------------------------------------------------------------------------
# the password must contains at least 1 symbol and not more than 4
# the password must contains at least 1 number and not more than 4
# chr() is a built function that convert ASCII code to its corresponding character.

import random

# user input loop ------------------------------------------------------------
userInput = True
while(userInput):
    try:
        passwordLength = int(input('Enter Password Length between 8 - 16: '))
        if passwordLength < 8 or passwordLength > 16:
            print ('Password Length must be between 8 and 16 try again !')
        else:
            userInput = False
    except:
        print('wrong input !')

        
# specify the length of symbols, numbers, and characters
while(True): # if both equal 4 then recalculate symbols and numbers length
    symbolsLength = random.randint(1,4)
    numbersLength = random.randint(1,4)
    if symbolsLength == 4 and numbersLength == 4:
        continue
    else:
        break
charactersLength = passwordLength - symbolsLength - numbersLength

# Generate password
passwordList = []

for i in range(symbolsLength):
    passwordList.append(chr(random.randint(35,38)))

for i in range(numbersLength):
    passwordList.append(chr(random.randint(48,57)))

for i in range(charactersLength):
    passwordList.append(chr(random.randint(97,122)))
    
random.shuffle(passwordList)
print(''.join(passwordList))
