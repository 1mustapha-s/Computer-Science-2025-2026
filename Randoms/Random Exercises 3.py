'''
Author: Mustapha
Date: 13 February 2026
Description: Random Exercises 3
'''


num1= input('Enter a 2 digit number : ')
num1_modified= num1[::-1]
num2= input('Enter another 2 digit number : ')
num2_modified= num2[::-1]
total= int(num1)**2 + int(num2)**2
total_modified= int(num2_modified)**2 + int(num1_modified)**2
print(f'The original sum is {total}')
print(f'The reversed sum is {total_modified}')
if total== total_modified:
    print('The sum of their squares equals the sum of the squares of their reversals' )
elif total== total_modified:
    print('The sum of their squares is not equal to the sum of the squares of their reversals')





