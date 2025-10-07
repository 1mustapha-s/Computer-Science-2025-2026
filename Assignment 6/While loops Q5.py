'''
Author: Mustapha
Date: 7 October 2025
Description: While loops exercise
'''


num= 1
while num != '':
    num= input('Enter any number: ')
    if num.isdigit():
        num= int(num)
        for i in range (1,num**2):
            if i == 50:
                break
            print(i)





