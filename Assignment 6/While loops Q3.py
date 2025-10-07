'''
Author: Mustapha
Date: 7 October 2025
Description: While loops exercise
'''


num= 1

while num != '':
    num= input('Enter any whole number: ')
    if num.isdigit():
        num= int(num)
        for i in range (0,num):
            if (i%2 == 0):
                print(i)










