'''
Author: Mustapha
Date: 7 October 2025
Description: While loops exercise
'''


num= 0
total= 0


while num < 50:
    num= int(input('Enter any number: '))
    total += num
    if total >= 50:
        break
    
print(total)








