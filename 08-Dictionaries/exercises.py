# 1. create an empty dictionary named dog
dog = {}

# 2. Add name, color, breed, legs and age to the dog dictionary
dog = {
    'name': 'Booba',
    'color': 'Black',
    'breed': 'Booby',
    'legs': 4,   
}
print(dog)

# 4. Get the length of the dog dictionary
dog = {
    'name': 'Booba',
    'color': 'Black',
    'breed': 'Booby',
    'legs': 4,   
}
print(len(dog))

# 5. Get the dictionary values as a list
dog = {
    'name': 'Booba',
    'color': 'Black',
    'breed': 'Booby',
    'legs': 4,   
}
key = dog.keys()
print(key)


# 10. Delete one of the items in the dictionary
dog = {
    'name': 'Booba',
    'color': 'Black',
    'breed': 'Booby',
    'legs': 4,   
}
dog.pop('breed')
print(dog)