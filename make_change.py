# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Christopher DeBetta
#               Colby Clayton
#               Jackson Bailey
#               Charlie Robertson

# Section:      ENGR-102-562
# Assignment:   Lab 2: Activity 1
# Date:         15 09 2022
#

#Get input values
myMoney = float(input('How much did you pay?')) * 100
cost = float(input('\nHow much did it cost?')) * 100
change = round(myMoney - cost)
print(f'\nYou received ${(change/100):.2f} in change. That is...')

#Calc change
pennies = 0
dimes = 0
nickels = 0
quarters = 0
while(change > 0):
    #print(change)
    if(change >= 25):
        quarters += 1
        change -= 25
    elif(change >= 10):
        dimes += 1
        change -= 10
    elif(change >= 5):
        nickels += 1
        change -= 5
    elif(change >= 1):
        pennies += 1
        change -= 1
if(quarters > 1):
    print(quarters, 'quarters')
elif(quarters == 1):
    print(quarters, 'quarter')
if(dimes > 1):
    print(dimes, 'dimes')
elif(dimes == 1):
    print(dimes, 'dime')   
if(nickels > 1):
    print(nickels, 'nickels')
elif(nickels == 1):
    print(nickels, 'nickel')  
if(pennies > 1):
    print(pennies, 'pennies')
elif(pennies == 1):
    print(pennies, 'penny')  