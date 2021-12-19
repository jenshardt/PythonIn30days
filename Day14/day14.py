'''
Created on 19.12.2021

@author: jens
'''

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

print(list(filter(is_even, numbers)))
print(list(filter(is_odd, numbers)))

numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

import functools
print(functools.reduce(add_two_nums, numbers_str))

names = ['Aachen', 'Köln', 'Hamburg', 'München']
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))