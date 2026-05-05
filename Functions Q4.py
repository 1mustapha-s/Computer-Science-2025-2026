'''
Author: Mustapha
Date: 1 May 2026
Description: Functions Question 4
'''


def name(a):
    if (len(a)>4):
        b= a.upper()
        a= a.replace(a[0],b[0])
        a= a.replace(a[3],b[3])
        
    else:
        a= False
    return a
a= input('Enter a name: ')
x= name(a)
print(x)




