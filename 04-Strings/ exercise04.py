# 1. Concatenating a string 
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
sentence = a + "" + b + "" + c + "" + d
print(sentence)

#  2. Concatenating a string
e = 'Coding'
f = 'For'
g = 'All'
h = ''
sentence_2 = e + h + f + h + g
print(sentence_2)

# 3. declare a variable and assign it to an initial value
# 4. print the variable
# 5. print the length of the variable
# 6. change all characters uppercase
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
# 7. change all characters to lowercase
print(company.lower())
# 8. capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9. slice the characters
slice = company.split()[0]
print(slice)
# 10. check is a string contains the word Coding using index, find or other methods
print(company.find('Coding'))
print(company.startswith('Coding'))
# 11. replace coding for all to python
replace_string = company.replace('Coding For All', 'Python')
print(replace_string)

# 12. change Python for Everyone to Python for All using the rplace method or other methods
challenge2 = 'Python for Everyone'
print(challenge2.replace('Python for Everyone', 'Python for All'))

# 31. which varaible returns true when we use the isidentier
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge3 = 'thirty_days_of_python'
print(challenge3.isidentifier())

# 33. tab escape sequence
print('Name\tAge\tCountry')
print('Lucy\t23\tSouth Africa')