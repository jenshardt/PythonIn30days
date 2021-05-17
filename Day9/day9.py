'''
Created on 17.05.2021

@author: jens
'''

a = 3
if a > 0:
    print('A is a positive number')

if a < 0:
    print('A is a negative number')
elif a == 0:
    print('A is zero')
else:
    print('A is (still) a positive number')
    
print('A is REALLY positive') if a > 0 else print('A is negative')

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive and odd integer')
        
points = int(input("Enter points: "))

if points < 0:
    print('What? Why? How?')
elif 0 <= points and points < 50:
    print('You earned that F!')
elif 50 <= points and points < 60:
    print('Yes - it is still a D!')
elif 60 <= points and points < 70:
    print('Very average C!')
elif 70 <= points and points < 90:
    print('Nice B!')
elif 90 <= points and points <= 100:
    print('Good work - an A!')
else:
    print('CHEATER!')
