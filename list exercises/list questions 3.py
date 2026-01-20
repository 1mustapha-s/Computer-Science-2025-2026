'''
Author: Mustapha
Date: 20 January 2026
Description: List Questions 3
'''

lst3= []
lst1= input('Enter a list: ')
lst2= input('Enter another list: ')
lst1= list(lst1)
lst2= list(lst2)
lst1.extend(lst2)
lst3.extend(lst1)
print(lst3)








