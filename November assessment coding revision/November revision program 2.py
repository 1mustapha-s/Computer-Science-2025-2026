'''
Author: Mustapha
Date: 17 December 2025
Description: November revision program 2
'''

#Step 1
wincard= '8549018035096133'
cardnum= wincard[:15]
last_digit= wincard[-1]

#Step 2
reverse= ''
for i in cardnum:
    reverse= i + reverse


#Step 3
even= ''
for i in range(0,15,2):
    even+= reverse[i]


odd= ''
for i in range(1,15,2):
    odd+= reverse[i]


totalodd= 0
for x in odd:
    x= int(x)
    odd= int(odd)
    totalodd+= x


totaleven= 0
for i in even:
    even= int(even)
    i= int(i)
    i=i*2
    if i>9:
        i= i-9
    totaleven+= i


#Step 4
last_digit= int(last_digit)
answer= totaleven+totalodd+last_digit

#Step 5
if (answer%10==0):
    print('This is a valid card')
elif (answer%10!=0):
    print('This is not a valid card')
else:
    print('Something went wrong, try again later')


















    
    
    
    
    
    
