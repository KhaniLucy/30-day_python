# Day 10-Loops- in programming we handle repetitive tasks by using loops
# there is while loop and for loop


# WHILE LOOP-is used to execute a block of statements repeatedly until a given condition is satisfied
# when a condition becomes false, the lines of code after the loop will be continued to be executed
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
# this while loop, the conditions becomes false when count is 5. That is when the loop stops

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# the above loop condition will be false when is 5 and the loop stops, and execution starts the else statement


# Break and Continue
# Break we use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# the while loop will only print 0, 1, 2 but when it reaches 3 it stops.

# continue- with the statement we can skip the current iteration, and continue with the next
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
# this loop will print 0, 1, 2, 4 skips 3


# For Loop- is used for iterating over a sequence(taht is either a list, a tuple, a dictionary, a set, or a string)
# for loop with list:
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# for loop with string
# syntax
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

# for loop with tuple:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# for loop with dicitonary
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
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# loop in a set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


# Break and Continue Part 2
# Break: we use break when we like to stop our loop before it is complicated
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break