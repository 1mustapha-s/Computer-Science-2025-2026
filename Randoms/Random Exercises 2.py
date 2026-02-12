'''
Author: Mustapha
Date: 12 February 2026
Description: Random Exercises 2
'''


import random
print('Welcome to my dice game!')
name= input('Enter your name: ')
lucky_number= int(input('Enter a lucky number (between 1 & 6): '))
computer_die_roll=random.randint(1,6) #initialize computer number
print(f'{name}\'s lucky number is {lucky_number}!')
print(f'Computer rolled a {computer_die_roll}!')
if computer_die_roll == lucky_number:
    print('You guessed correct!')
elif computer_die_roll > lucky_number:
    print('You guessed too low!')
elif computer_die_roll < lucky_number:
    print('You guessed too high!')
















