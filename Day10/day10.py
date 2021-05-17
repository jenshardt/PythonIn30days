'''
Created on 17.05.2021

@author: jens
'''

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    
for number in range(11):
    print(number)
    
sum_odd = 0
sum_even= 0

for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

print('The sum of all evens is', sum_even, '. And the sum of all odds is', sum_odd, ' (Calculated 1 to', len(range(101))-1, ')')

rows = int(input('Row count'))
columns = int(input('Column count'))
current_row = 0
row_string = ''

while current_row < rows:
    row_string += '# '
    current_row += 1

current_column = 0
while current_column < columns:
    print(row_string)
    current_column += 1