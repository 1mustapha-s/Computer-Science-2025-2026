'''
Author: Mustapha
Date: 6 October 2025
Description: While loops exercise
'''


grade= 2
count= 0
total= 0

while grade != '' :
    grade= input('Enter your grade: ')
    if grade.isdigit():
        grade=int(grade)
        total= total+grade
        count+=1
average= (total/count)
print(average)