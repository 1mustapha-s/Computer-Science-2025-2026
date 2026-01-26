'''
Author: Mustapha
Date: 26 January 2026
Description: List Questions 11
'''

#Part A
str_list= ['apple']
add= eval(input('Enter an element to add to the list: '))
str_list.append(add)
print(max(str_list))

#Part B
l2= []
l= [1,2,3,4,5,6,7,8,9,10]
num= int(input('Enter a number: '))
for i in l:
    i= i+num
    l2.append(i)
print('Original list:',l)
print('Modified list:',l2)


