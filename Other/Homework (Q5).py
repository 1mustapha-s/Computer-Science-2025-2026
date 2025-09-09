'''
Author: Mustapha
Date: 3 September 2025
Description: If, else, elif excercise
'''

rain= input('Hello, is it raining? ')
rain= str(rain)
if(rain=='Yes') or (rain=='yes'):
    windy= input('Is it windy? ')
    windy= str(windy)
    if(windy=='Yes') or (windy=='yes'):
        print('It is too windy for an umbrella ')
    elif(windy!='Yes') or (windy!='yes'):
        print('Take an umbrella ')
else:
    print('Enjoy your day ')
    


