'''
Author: Mustapha
Date: 8 January 2026
Description: List Exercises
'''

#Appending a single item to a list
lst1 = [10, 12, 14]
lst1.append(16)

#Appending a list to elements of a list
val= [17,24,15,30]
val.extend([34,27])

#Inserting an element in a list
val2= [17,24,15,30]
val2.insert(2,33)

#Modifying/updating elements in a list
lst2= [10,12,14,16]
lst2[2]= 24

#Deleting an element using its index/position
val3= [17,24,15,30]
val3.pop(2)

#Deleting an element using its value
val4= [17,24,15,30]
val4.remove(24)

#Deleting a sublist from a list
lst3= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst3[10]
del lst3[10:15]





