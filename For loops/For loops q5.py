'''
Author: Mustapha
Date: 8 September 2025
Description: for loops excercise
'''


total= 0
total= float(total)


num1= input('Enter any number to add to the total ')
num1= float(num1)
confirm= input('Would you like to add this number to the total? Type yes or no ')
confirm= str(confirm)
if(confirm== 'Yes') or (confirm== 'yes'):
    total= total+num1 
    print('Number has been added ')
elif(confirm!= 'Yes') or (confirm!= 'yes'):
    print('Number not added ')
    
num2= input('Enter the second number ')
num2= float(num2)
confirm= input('Would you like to add this number to the total? Type yes or no ')
confirm= str(confirm)
if(confirm== 'Yes') or (confirm== 'yes'):
    total= total+num2
    print('Number has been added ')
elif(confirm!= 'Yes') or (confirm!= 'yes'):
    print('Number not added ')
    
num3= input('Enter the third number ')
num3= float(num3)
confirm= input('Would you like to add this number to the total? Type yes or no ')
confirm= str(confirm)
if(confirm== 'Yes') or (confirm== 'yes'):
    total= total+num3
    print('Number has been added ')
elif(confirm!= 'Yes') or (confirm!= 'yes'):
    print('Number not added ')
    
num4= input('Enter the fourth number ')
num4= float(num4)
confirm= input('Would you like to add this number to the total? Type yes or no ')
confirm= str(confirm)
if(confirm== 'Yes') or (confirm== 'yes'):
    total= total+ num4
    print('Number has been added ')
elif(confirm!= 'Yes') or (confirm!= 'yes'):
    print('Number not added ')
    
num5= input('Enter the final number ')
num5= float(num5)
confirm= input('Would you like to add this number to the total? Type yes or no ')
confirm= str(confirm)
if(confirm== 'Yes') or (confirm== 'yes'):
    total= total+num5
    print('Number has been added ')
elif(confirm!= 'Yes') or (confirm!= 'yes'):
    print('Number not added ')


print('The total is', total)





