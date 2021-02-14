'''
Created on 14.02.2021

@author: jens
'''

first_name = 'Jens'
last_name = 'Hardt'
full_name = first_name + ' ' + last_name
country = 'Germany'
city = 'Cologne'
age = 42
year = 2021
is_married = False
is_true = True
is_light_on = False
var_a, var_b, var_c =  10, 'dog', ['a','b','c']

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(is_married))
print(type(var_a))
print(type(var_b))
print(type(var_c))

print('Length of first_name is', len(first_name))
print('Length of last_name is', len(last_name))

num_one = 5
num_two = 4
_total = num_one + num_two
_diff = num_one + num_two
_product = num_one * num_two
_division = num_one / num_two

first_name = input("your first name?")

print('Length of first_name is now', len(first_name))

help('keywords')