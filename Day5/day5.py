'''
Created on 17.02.2021

@author: jens
'''
import statistics

myList = list()
print('Items in myList:', len(myList))

myNewList = ['a', 'b', 'c', 'd']
print('Items in myNewList:', len(myNewList))
print('myNewList:', myNewList)
print('First item in myNewList from the back: ', myNewList[0])
print('Second item in myNewList from the start: ', myNewList[1])
print('Second item in myNewList from the back: ', myNewList[-2])
print('Last item in myNewList: ', myNewList[-1])

# Unpacking List Items
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# Slicing Items from a List
fruits = ['banana', 'orange', 'lime', 'kiwi']
all_fruits = fruits[-4:]
print(all_fruits)

orange_and_lime = fruits[-3:-1]
print(orange_and_lime)

reverse_fruits = fruits[::-1]
print(reverse_fruits)

does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'mango' in fruits
print(does_exist)

fruits.append('mango')
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

fruits.clear()
print(fruits)

fruits = ['gherkin', 'orange', 'lime', 'kiwi']
vegetables = ['tomato', 'potato', 'onion', 'carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

print(fruits.index('orange'))

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# Excercise lvl 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
print('min_age: ', min_age)
max_age = ages[-1]
print('max_age: ', max_age)
               
#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
median = statistics.median(ages)
print('median: ', median)

#Find the average age (sum of all items divided by their number)
average = sum(ages) / len(ages)
print('average: ', average)

#Find the range of the ages (max minus min)
range = ages[-1] - ages[0]
print('range: ', range)

#Compare the value of (min - average) and (max - average), use abs() method
value_1 = abs(min_age - average)
value_2 = abs(max_age - average)
print('min - average: ', value_1)
print('max - average: ', value_2)