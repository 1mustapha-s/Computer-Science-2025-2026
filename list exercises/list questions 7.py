'''
Author: Mustapha
Date: 23 January 2026
Description: List Questions 7
'''


#Part A
lstA= []
for i in range(0,50):
    lstA.append(i)
print(lstA)

#Part B
lstB=[]
for i in range(1,51):
    x= i**2
    lstB.append(x)
print(lstB)

#Part C
x= 1
lstC2= []
lstC= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in lstC:
    i= i*x
    lstC2.append(i)
    x+=1
    
print(lstC2)





