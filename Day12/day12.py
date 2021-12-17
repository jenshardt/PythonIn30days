'''
Created on 17.12.2021

@author: jens
'''

import mymodule
print(mymodule.generateFullName('Bart', 'Simpson'))

from mymodule import sumTwoNumbers as total
print(total(2, 4))

# os module
import os
# DOS mkdir
os.mkdir('directory_name')
# Changing the current directory
os.chdir('directory_name')
# Getting current working directory
print(os.getcwd())
# Jumping up
os.chdir('..')
# Removing directory
os.rmdir('directory_name')

# statistics module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# math module
from math import *
print(pi)           # 3.141592653589793, pi constant
print(sqrt(2))      # 1.4142135623730951, square root
print(pow(2, 3))    # 8.0, exponential function
print(floor(9.81))  # 9, rounding to the lowest
print(ceil(9.81))   # 10, rounding to the highest
print(log10(100))   # 2, logarithm with 10 as base

# random module
from random import random, randint
print(random())
print(randint(1,10))