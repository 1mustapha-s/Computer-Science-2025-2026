'''
Author: Mustapha
Date: 7 May 2026
Description: Function excercise 2
'''


lst= eval((input('Enter some numbers: ')))
lst= list(lst)
print(f'List: {lst}')

#1
rang= 0
def ran(rang):
    rang= max(lst) - min(lst)
    return rang
x= ran(lst)
print(f'Range: {x}')


#2
av= 0
def avg(av):
    av= round((sum(lst) / len(lst)),2)
    return av
y= avg(av)
print(f'Average: {y}')


#3
med= 0
def median(med):
    a= sorted(lst)
    if (len(a)%2==0):
        med= len(a)/2
        index= int(round(med,1))
        med= (a[index] + a[index-1])/2
    elif (len(a)%2!=0):
        index= int(round((len(a)/2),1))
        med= a[index]
    return med
z= median(med)
print(f'The median: {z}')



#4
mode= 0
def mode(a):
    for i in a:
        mode= lst.count(i)
        if mode > 1:
            mode= i
            break
        else:
            mode= 'N/A'
    return mode
v= mode(lst)
print(f'Mode: {v}')
        

#5
def freq(a):
    for i in a:
        







