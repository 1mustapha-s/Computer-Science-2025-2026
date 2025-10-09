'''
Author: Mustapha
Date: 9 October 2025
Description: While loops exercise
'''


num= 67
guess= 0
while num != '':
    guess= input('Guess my number: ')
    if guess.isdigit():
        guess = int(guess)
        if (guess == num):
            print('Well done you are a genius')
            break
        elif (guess < num):
            print('Too low')
        elif (guess > num):
            print('Too high')
else:
    print('You did something wrong')







