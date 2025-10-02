'''
Author: Mustapha
Date: 2 October 2025
Description: While loops exercise
'''
number = 2
total = 0
count = 0
while number!= '':
    number == input('Enter any number: ')
    if number.isdigit():
        total += int(number)
        count += 1
print('Average is: ', total/count)





