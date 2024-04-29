# Dictionaries is a collection of unordered, modified(mutable) paired (key:value) data type.

# Creating a Dictionary
# To create a dictionary we use curly brackets, {} or the dict() built-in function
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street ext 14',
        'zipcode':'1818'
    }
    }
# the dictionary above shows that a value could be any data type: string, boolean, list, tuple, set or a dictionary


# Dictionary Length- checks the number of "key: value" pairs in the dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street',
        'zipcode':'1818'
    }
    }
print(len(person)) # 7


# Accessing Dictionary Items- we can access dictionary items by referring to its key name

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street',
        'zipcode':'1818'
    }
    }
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][2])
print(person['address']['street'])
print(person['city'])

# get()method to access values in a dictionary
person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street',
        'zipcode':'1818'
    }
    }
print(person.get(['first_name']))
print(person.get('country'))
print(person.get('skills'))
print(person('city'))


# Adding items to a Dictionary- we can add new key and value pairs to a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street',
        'zipcode':'1818'
    }
    }
person['job_title'] = 'Software Developer'
person['skills'].append('Python')
print(person)


# Modifying items in a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street',
        'zipcode':'1818'
    }
    }
person['first_name'] = 'Verotia'
person['age'] = 23
print(person)


# Checking keys in a Dictionary- we use the in operator to check if a key exists in a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False


# Removing key and value pair from dictionary
# pop(key): removes the item with the specified key name
# popitem(): removes the last item
# del: removes an item with specified key name
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
person = {
    'first_name':'Lucy',
    'last_name':'Swele',
    'age':24,
    'country':'South Africa',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'17727 Robin Street',
        'zipcode':'1818'
    }
    }
person.pop('first_name')
person.popitem()
del person['is_namrried']


# Changing Dictionary to a list of items- items() method changes dictionary to a list of tuples
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])


# Clearing a dictionary- if we don't want the items in a dictionary we can clear them using clear()method
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None


# Deleting a dictionary- if we do not use the dictionary we can delete it completely
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct


# Copy a Dictionary- we can copy a dictionary using a copy() method.
# using copy we can avoid mutation of the origianl dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


# Getting Dictionary keys as a list
# keys() method gives us all the keys of a dictionary as a list
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])


# Getting Dictionary Values as a List
# value method gives us all the values of a dictionary as a list
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

