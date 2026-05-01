'''
Author: Mustapha
Date: 30 April 2026
Description: Functions Question 2
'''

a=''
def animals(a):
    space = a.find(' ')
    space= space +1
    return space
a= input('Enter a 2 word string: ')
x= animals(a)
if a[0] == a[x]:
    print('True')
else:
    print('False')
    
    







