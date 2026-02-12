'''
Author: Mustapha
Date: 9 February 2026
Description: Random Exercises
'''


import random

#1
print(random.randint(1,100))

#2
fruits= ['apple','banana','orange','pineapple','peach']
print(random.choice(fruits))

#3
z= ''
x= random.randint(0,1)
if x == 0:
    z= 'Tails'
elif x == 1:
    z= 'Heads'
y= input('Heads or Tails. Enter 1 for heads, 0 for tails: ')
y= int(y)
if y == x:
    print(f'You win! The answer was {z}!')
elif y != x:
    print(f'You lose! The answer was {z}!')

#4
guess= ''
num= random.randint(1,100)
tries = 7
while (tries>0):
    guess= input(f'Guess the number between 1 an 100, you have {tries} attempt(s) left: ')
    guess= int(guess)
    tries-=1
    if guess == num:
        print('You got it right!')
        break 
    elif guess != num:
        print('Try again')
        
#5
print('Welcome to maths quiz! Type q to quit!')
solution= 0
q= False
score= 0
ans= 0
lst= ['+','-','/','*']
while q != True:
    num1= random.randint(1,100)
    num2= random.randint(1,100)
    operator= random.choice(lst)
    if operator== '+':
        solution= num1 + num2
    elif operator == '-':
        solution= num1 - num2
    elif operator== '/':
        solution == num1 // num2
    elif operator == '*':
        solution = num1 * num2
    ans= input(f'Calculate {num1} {operator} {num2}: ')
    if ans == 'q':
        break
    ans= int(ans)
    if ans== solution:
        score+=1
        print(f'{solution} is correct! Score: {score}')
    elif ans!= solution:
        print(f'{ans} is incorrect! The answer was {solution}! Score: {score}')





