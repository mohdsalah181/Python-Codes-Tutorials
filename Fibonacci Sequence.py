### Fibonacci Sequence ------------------------------------------------ ###

FebSequence = [0, 1]
Fn = 0

while True:
    if Fn >= 2:
        break
    try:
        while Fn < 2:
            Fn = int(input('Enter Fibonacci Number equal to or greater than 2: '))
    except:
        print('\nplease enter number')
        



for i in range(2, Fn+1):
    FNum = FebSequence[i-1] + FebSequence[i-2]
    FebSequence.append(FNum)

print(FebSequence)
