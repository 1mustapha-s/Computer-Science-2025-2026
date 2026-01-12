'''
Author: Mustapha
Date: 12 January 2026
Description: List Exercises 5
'''


lst = eval(input("Enter list: "))
length = len(lst)
mean = sum = 0
for i in range(0, length):
    sum += lst[i]
mean = sum / length
print("Given list is: ", lst)
print("The mean of the given list is:", mean)







