# Password Generator
#---------------------------------------
# chr() is a built function that convert ASCII code to its corresponding character.
# shuffle is a method that takes a sequence like a list and reorderize its items.

import random

def passwordShuffle(password):
    passwordList = list(password)
    random.shuffle(passwordList)
    return ''.join(passwordList)

capitalChar1 = chr(random.randint(65,90))
capitalChar2 = chr(random.randint(65,90))
smallChar1 = chr(random.randint(97,122))
smallChar2 = chr(random.randint(97,122))
num1 = chr(random.randint(48,57))
num2 = chr(random.randint(48,57))
symbol1 = chr(random.randint(35,38))
symbol2 = chr(random.randint(35,38))


password = capitalChar1 + capitalChar2 + smallChar1 + smallChar2 + num1 + num2 + symbol1 + symbol2
print(passwordShuffle(password))
