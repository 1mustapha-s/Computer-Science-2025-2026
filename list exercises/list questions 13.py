'''
Author: Mustapha
Date: 27 January 2026
Description: List Questions 13
'''

lst2= []
lst= eval(input('Enter a list of integers: '))
i= int(input('Enter an index: '))
j= int(input('Enter another index: '))
lst2= lst[i:j]
maxl= max(lst2)
minl= min(lst2)
print(f'The minimum value from the range is {minl}, the maximum is {maxl}')

