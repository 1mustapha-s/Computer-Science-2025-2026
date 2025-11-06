'''
Author: Mustapha
Date: 5 November 2025
Description: A12 String operations Q12
'''


string= input('Enter a string with brackets: ')
brackets= string.count('(')
brackets2= string.count(')')
if brackets==brackets2:
    print('It has the same number of opening and closing parenthesis')
elif brackets!=brackets2:
    print('It does not have the same number of opening and closing parenthesis')
else:
    print('Something went wrong')
    









