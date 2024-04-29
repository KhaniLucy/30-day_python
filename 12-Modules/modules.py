# Module- is a file containing a set of codes or a set of functions which can be included to an application.
# a module can be a file containing a single variable, a function or a big code base.


# Creating a Module- to create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder.
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
# create main.py file in your project directory and import the mymodule.py


# Importing a Module- to import the file we use the import keyword and the name of the file only.
# main.py file
#import mymodule
#print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh


# Import functions from a Module- we can have many functions and we can import all the functions differently
# main.py file
#from mymodule import generate_full_name, sum_two_nums, person, gravity
#print(generate_full_name('Asabneh','Yetayeh'))
#print(sum_two_nums(1,9))
mass = 100;
#weight = mass * gravity
#print(weight)
#print(person['firstname'])


# Importing functions from a module and renaming- during importing we can rename the name of the module
# main.py file
"""from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])""" 

