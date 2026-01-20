'''
Author: Mustapha
Date: 20 January 2026
Description: List Questions 1
'''
list2= []
list1= [1,2,3,4]
print(f'Original list: {list1}')
num= input('Enter a number to increment list values by: ')
num= int(num)
for i in list1:
    i= i+ num
    list2.append(i)
print(list2)





