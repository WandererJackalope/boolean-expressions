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

a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))

aOut = ""
bOut = ""
cOut = ""
#Format A
if(a < 0):
    aOut += "- "
if(abs(a) == 1):
    aOut += "x^2 "
elif(a != 0):
    aOut += str(abs(a)) + "x^2 "

#Format B
if(b < 0 and a!= 0):
    bOut += "- "
elif(b > 0 and a != 0):
    bOut += "+ "
if(abs(b) == 1):
    bOut += "x "
elif(b != 0):
    bOut += str(abs(b)) + "x "

#Format C
if(c < 0):
    cOut += "- "
elif(c > 0 and b != 0):
    cOut += "+ "
if(c != 0):
    cOut += str(abs(c)) + " = 0"
else:
    cOut += "= 0"

print("The quadratic equation is " + aOut + bOut + cOut)

