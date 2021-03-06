'''
Created on 17.02.2021

@author: jens
'''


empty_set = {}
preset_set = {'1', '2', '3', '4'}

print(len(preset_set))

fruits = {'banana', 'orange', 'mango', 'lemon'}
print("Is there a mango in the set?", 'mango' in fruits)

print(fruits)
fruits.update({'kiwi', 'apple'})
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

del fruits
# print(fruits) - NameError: name 'fruits' is not defined

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}

print(st1.intersection(st2))

print(st1.difference(st2))

print(st2.difference(st1))

print(st2.issubset(st1))

print(st1.issuperset(st2))