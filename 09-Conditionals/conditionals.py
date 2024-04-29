# Day 09- Conditonals
# By default statements in Python scripts are executed sequentially from top to bottom.
# the flow of execution can be altered in two ways:
# Conditional execution: a block of one or more statements will be executed if a certain experession is TRUE.
# Repetitive execution: a block of none or more statements will be reptitively executed as long as a certain expression is TRUE. In comprassion and logical operators 


# If Condition- in programming the keyword (if) is used to check if a condition is true and to execute the block code.
# syntax
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number- 3 is greater than zero. the condition was true and the block code was executed
# should the condition be false we do not see the result- 


# If Else- if the condition is true the first block will be executed, it not the else condtion will run
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# the condition above proves false, therefore the else block was excuted.
# How about if our condition is more than two- we could use elif

# If Elif Else-
# In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


# Short Hand
# syntax
# code if condition else code


# Nested Condtions- conditions can be nested
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
# we can avoid writing nested condition by using logical operator and.


# If Condition and Logical Operator 
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')