'''
Author: Mustapha
Date: 9 January 2026
Description: List Exercises 1
'''

myl= [2,4,6]
print(f'Existing list is: {myl}')
n= eval(input('Enter a number or list to be appended: '))
if type(n)== type([]):
    myl.extend(n)
elif type(n)== type(1):
    myl.append(n)
else:
    print('Please enter either an integer or a list.')
print(f'Appended list is: {myl}')



