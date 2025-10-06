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

if average >= 90:
    print('A')
elif (average <= 89) and (average >=80):
    print('B')
elif (average <=79) and (average >=70):
    print('C')
elif (average <=69) and (average >=60):
    print('D')
elif (average <=59):
    print('F')
else:
    print('Something is not right')
