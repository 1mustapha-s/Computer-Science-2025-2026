'''
Author: Mustapha
Date: 26 January 2026
Description: List Questions 10
'''

f= []
count= 0
one= 1
zero= 0
n= int(input('Enter a value to be found in the Fibonacci series: '))
nexta = zero  
count = 1

while count <= n:
    count += 1
    zero, one = one, nexta
    nexta = zero + one
print(nexta)









