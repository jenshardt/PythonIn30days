'''
Created on 06.03.2021

@author: jens
'''

empty_tupel = ()
preset_tupel = ('1', '2', '3')

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
another_first_fruit = fruits[0]

second_fruit = fruits[-3]

last_fruit = fruits[-1]

#  Tuple is immutable if we want to modify a tuple we should change it to a list
print(fruits)
# fruits[0] = 'apple' - this is an error as a 'tuple' object does not support item assignment

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)

fruits = tuple(fruits)
print(fruits)

print('orange' in fruits)
print('banana' in fruits)
