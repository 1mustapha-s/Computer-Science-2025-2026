# Please enter name: Mustapha
print("******************")
print("* Conversions *")
print("******************")
print("1) From teaspoons to ml")
print("2) From tablespoons to ml")
print("3) From cups to ml")
print("4) From ml to teaspoons")
print("5) From ml to tablespoons")
print("6) From ml to cups")
conversion = int(input("Please enter the conversion. e.g entering (3) will convert cups to ml: "))
if conversion == 1:
    teaspoons = float(input("Please enter number of teaspoons:"))
    ml = teaspoons * 5
    print("The ml is:", ml)
elif conversion == 2:
    tablespoons = float(input("Please enter number of tablespoons:"))
    ml = tablespoons * 15
    print("The ml is:", ml)
elif conversion == 3:
    cups= float(input("Please enter number of cups:"))
    ml = cups*210
    print(f'The ml is: {ml}')
elif conversion == 4:
    ml= float(input('Please enter number of ml: '))
    teaspoons= ml/5
    print(f'The teaspoons are: {teaspoons}')
elif conversion == 5:
    ml= float(input("Please enter number of ml: "))
    tablespoons= ml/15
    print(f'The tablespoons are: {tablespoons} ')
elif conversion == 6:
    ml = float(input("Please enter number of ml "))
    cups = ml/210
    print(f'The number of cups is: {cups} ')
    
    
    
    
