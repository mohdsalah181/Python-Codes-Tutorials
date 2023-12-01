import time

def countDown(t):
    while t:
        min, sec = divmod(t, 60)
        print('{:02d}:{:02d}'.format(min,sec),end="\r")
        time.sleep(1)
        t-=1
    print('Timer Finished')

userInput = input('Enter time in seconds: ')
countDown(int(userInput))
