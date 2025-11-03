'''
Author: Mustapha
Date: 3 November 2025
Description: A11 String operations Q3
'''

total= 0
word= input('Enter a word: ')
for letter in word:
    if letter.isdigit():
        letter= int(letter)
        total= total+letter
print(total)
        





