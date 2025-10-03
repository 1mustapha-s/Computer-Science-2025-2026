'''
Author: Mustapha
Date: 3 October 2025
Description: While loops exercise
'''
num = 2
total = 0
count = 0

while num !='':
    num= input('Enter any number: ')
    if num.isdigit():
        total+= int(num)
        count+= 1
print('Average is: ', total/count)





