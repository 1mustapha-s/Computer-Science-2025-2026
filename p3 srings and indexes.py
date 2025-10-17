'''
Author: Mustapha
Date: 17 October 2025
Description: Assignment 9
'''


word= input('Enter any word: ')
if word[0] in 'AaEeIiOoUu':
    print(word+'way')
else:
    wordnew= ''
    for i in range(1,len(word)):
        wordnew= wordnew+word[i]
    wordnew= wordnew+word[0]
    print(wordnew+'ay')



