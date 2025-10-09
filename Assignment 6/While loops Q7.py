'''
Author: Mustapha
Date: 9 October 2025
Description: While loops exercise
'''


num= 0
while num != '':
    num= input('Enter a number between 10 and 20: ')
    if num.isdigit():
        num= int(num)
        if (num >= 10) and (num <= 20):
            print('Thank you')
            break
        elif (num < 10):
            print('Too low')
        elif (num > 20):
            print('Too high')
        else:
            print('You did something wrong')
        











