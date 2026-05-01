'''
Author: Mustapha
Date: 1 May 2026
Description: Functions Question 3
'''


result= ''
def twenty(a,b):
    if (a+b==20) or (a==20) or (b==20):
        result= 'True'
    else:
        result= 'False'
    return result
a= int(input('Enter 1 number: '))
b= int(input('Enter a 2nd number: '))
x= twenty(a,b)
print(x)



