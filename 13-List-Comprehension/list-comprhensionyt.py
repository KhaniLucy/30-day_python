'''LIST COMPRHENSION'''
# allows you to create a new list with compact syntax and is based on the vales of an existing list


# find the squares of this numbers
num = [1,2,3,4]
sq = []
for n in num:
    sq.append(n**2)
print(sq)
# output should be [1,4,9,16]


# using the list comprehension method
num = [1,2,3,4,5]
sq = [n**2 for n in num]
print(sq)
# output is [1,4,9,16,25]


# finding letters
n_letters = []
for letter in 'Simplilearn':
    n_letters.append(letter)
print(n_letters)
# output is ['S', 'i', 'm', 'p', 'l', 'e', 'a', 'r', 'n']


n_letters = [letter for letter in 'Simplilearn']
print(n_letters)
# output is ['S', 'i', 'm', 'p', 'l', 'e', 'a', 'r', 'n']


# using a for loop
cars = ["Jaguar", "Land Rover", "Tesla", "Toyot", "Tata"]
newlist = []
for x in cars:
    if "s" in x:
        newlist.append(x)
print(newlist)
# output is "Tesla"

cars = ["Jaguar", "Land Rover", "Tesla", "Toyot", "Tata"]
newlist = [x for x in cars if "s" in x]
print(newlist)
# output is Tesla
# remember python is case sensitive


new_list = [x for x in range(100) if x > 50]
print(new_list)     # aim is to print integars that are greater than 50

new_list = [x for x in range(100) if x < 30]
print(new_list)


# this method changes a variable inside the list value
cars = ["Jaguar", "Land Rover", "Tesla", "Toyot", "Tata"]
new_cars = [x if x != "Tesla" else "Audi" for x in cars]
print(new_cars)
# output is Jaguar, Land Rover, Audi, Toyota, Tata


# using function 
number = []
for i in range(0, 20):
    number.append(i%2==0)
print(number)
# if the number is even it will print out true and if it a ood number it will be false

# using the list comphrension method
numbers = [i%2==0 for i in range(0, 21)]
print(numbers)


import numpy as np # type: ignore
A = np.random.randint(10, size=(4,4))
print(A)

max_element = [max(i) for i in A]
max_element