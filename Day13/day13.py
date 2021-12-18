'''
Created on 17.12.2021

@author: jens
'''

language = 'Python'
lst = list(language)
print(type(lst)) 
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

# generate even numbers list in range 0 to 21
even_numbers = [i for i in range(21) if i % 2 == 0]  
print(even_numbers)

# Lambda functions
# oldschool
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))

# same as lambda function
add_two_nums_lambda = lambda a, b: a + b
print(add_two_nums_lambda(2,3))

def power(x):
    return lambda n : x ** n

# function power now need 2 arguments to run, in separate rounded brackets
print(power(2)(3))
print(power(2)(6))
print(power(1)) # result is <function power.<locals>.<lambda> at 0x000001E8D23EB670>