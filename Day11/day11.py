'''
Created on 18.05.2021

@author: jens
'''

# print(add_two_numbers()) - not allowed!

def add_two_numbers (num_one = 0, num_two = 0):
    total = num_one + num_two
    return total

print(add_two_numbers(2, 3))
print(add_two_numbers()) # works because of default values
print(add_two_numbers(1))

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True
    return False

print('10 is even:', is_even(10))
print('7 is even:', is_even(7))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(2, 3, 5))
