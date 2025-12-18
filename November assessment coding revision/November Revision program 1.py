'''
Author: Mustapha
Date: 15 December 2025
Description: November revision program 1
'''
#Step 1
wincard= '8549018035096133'
cardnum= wincard[:15]
last_digit= wincard[-1]


#Step 2
reverse= cardnum[::-1]

#Step 3
odd= reverse[1::2]
even= reverse[::2]


totalodd= 0
totaleven= 0
empty= ''

for i in even:
    even= int(even)
    i= int(i)
    i=i*2
    if i>9:
        i= i-9
    totaleven+= i

for x in odd:
    odd= int(odd)
    x= int(x)
    totalodd+= x
    
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
















