'''
Created on 19.12.2021

@author: jens
'''

# Python Error Types

# -> SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
# print 'hello world' 

# -> NameError: name 'age' is not defined
# print(age)

# -> IndexError: list index out of range
numbers = [1, 2, 3, 4, 5]
# numbers[5]

# -> ModuleNotFoundError: No module named 'maths'
# import maths

# -> AttributeError: module 'math' has no attribute 'PI'
import math
# math.PI

# -> KeyError: 'county'
users = {'name':'Sauron', 'age':2500, 'country':'Mordor'}
# users['county']

# -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 4 + '3'

# -> ImportError: cannot import name 'power' from 'math'
# from math import power

# -> ValueError: invalid literal for int() with base 10: '12a'
# int('12a')

# -> ZeroDivisionError: division by zero
# 1/0