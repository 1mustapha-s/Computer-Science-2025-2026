'''
Author: Mustapha
Date: 5 September 2025
Description: If, else, elif excercise
'''

num= input('Enter a number: ')
num= float(num)
if(num>=10) and (num<=20):
    print('Correct')
elif(num<10):
    print('Too low')
elif(num>20):
    print('Too high')
else:
    print('Invalid')

