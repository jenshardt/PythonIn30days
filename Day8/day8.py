'''
Created on 17.02.2021

@author: jens
'''

person = {
    'first_name':'Jens',
    'last_name':'Hardt',
    'age':42,
    'country':'Mordor',
    'is_married':False,
    'skills':['Java', 'C++', 'COBOL', 'MongoDB', 'DB2', 'Oracle', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'12345'
    }
}

print(len(person))

print(person.get('country'))
print(len(person.get('skills')))
print(person.get('address').get('street'))
print(person.get('city'))
# print(person.get('city').get('area')) - AttributeError: 'NoneType' object has no attribute 'get'

person['address']['city'] = 'Mars'
person['skills'].append('SpringBoot')

print(person)

person.pop('is_married')

print(person)

# person.pop('is_married') - KeyError: 'is_married'

values = person.values()
print(values)

keys = person.keys()
print(keys)