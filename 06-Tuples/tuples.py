# A tuple is a collection of different data types which is oreded and unchangeable(immutable).
# tuples are written with round brackets(). once a tuple is created we cannot change its values
# we cannot use add, insert, remove methods in a tuple because it is not modifiable(mutable)

# tuple()- to create an empty tuple
# count()- to count the number of specified item in a tuple
# index()- to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple


# CREATING A TUPLE

# empty tuple: creating and empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# tuple with initial values
# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')


# tuple length- use the len() {function} to get the length of a tuple
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)


# accessing tuples in a positive way
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]


# accessing tuples in a negative way
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]


# slicing tuples- we slice out a sub-tuple by specfing a range of indexes where to start and where to end in a tuple, the return value will be a new tuple with the specified items
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# range of negative indexes
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]


# changing tuples to lists
# we can change tuples to lists and lists to tuples.- they only modified if they being changed to lists
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


# checking an item in a tuple- checking if an item exists or not using in, it returns a boolean 
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment


# join tuples- we join two or more tuples using +operator: concatenation
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables


# deleting tuples- its not possible to remove a single item in a tuple but it is possible to delete the tuple using del keyword.
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits