'''
Author: Mustapha
Date: 3 November 2025
Description: A11 String operations Q4
'''

tries= 7
num= 17
while tries!=0:
    guess= input('Guess a number between 1 and 100: ')
    if guess.isdigit():
        guess= int(guess)
        if guess== num:
            print('Well done')
            tries-= 1
            break
        elif guess<num:
            tries-= 1
            print(f'Too low, {tries} attempt(s) left')
        elif guess>num:
            tries-= 1
            print(f'Too high, {tries} attempt(s) left')
            
            
        









