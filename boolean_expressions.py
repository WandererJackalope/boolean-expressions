# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jackson Bailey
#               Colby Clayton
#               Chris Debetta
#               Charlie Robertson
# Section:      562
# Assignment:   Lab 4.15
# Date:         23 Sep 2022
############ Part A ############
a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')
# Convert a var from str to bool
if a == 'True':
    a = True
elif a == 'T':
    a = True
elif a == 't':
    a = True
elif a == 'False':
    a = False
elif a == 'F':
    a = False
elif a == 'f':
    a = False
# Convert b var from str to bool
if b == 'True':
    b = True
elif b == 'T':
    b = True
elif b == 't':
    b = True
elif b == 'False':
    b = False
elif b == 'F':
    b = False
elif b == 'f':
    b = False
# Convert c var from str to bool
if c == 'True':
    c = True
elif c == 'T':
    c = True
elif c == 't':
    c = True
elif c == 'False':
    c = False
elif c == 'F':
    c = False
elif c == 'f':
    c = False
############ Part B ############
print(f'a and b and c: {a and b and c}')
print(f'a or b or c: {a or b or c}')
############ Part C ############
print(f'XOR: {a is not b}')
print(f'Odd number: {(a + b + c) % 2 == 1}')
############ Part D ############

