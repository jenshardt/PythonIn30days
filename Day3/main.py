'''
Created on 14.02.2021

@author: jens
'''

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))


print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

print('1 is 1', 1 is 1) # SyntaxWarning: "is" with a literal. Did you mean "=="?
print('1 is not 2', 1 is not 2) # SyntaxWarning: "is not" with a literal. Did you mean "!="?
print('J in Jens', 'J' in 'Jens')
print('j in Jens', 'j' in 'Jens')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2:', 4 is 2 ** 2) # SyntaxWarning: "is" with a literal. Did you mean "=="?

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height

print("The area of the triangle is {0:.0f}".format(area))