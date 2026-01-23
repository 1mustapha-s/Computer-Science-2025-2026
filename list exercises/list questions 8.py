'''
Author: Mustapha
Date: 23 January 2026
Description: List Questions 8
'''


lstN= []
lstL= eval(input('Enter a list of numbers: '))
lstM= eval(input('Enter another list of numbers of the same size: '))
x=0
for i in lstL:
    i= i+lstM[x]
    x+=1
    lstN.append(i)
print(lstN)



