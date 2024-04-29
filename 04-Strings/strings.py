# Creating a string 

letter = 'G'     # A string can be a single character or bunch of texts
print(letter)    # G
print(len(letter)) # 1 - prints out the number of characters
greetings = 'Dumelang Sechaba'  # A string can be made usingsingle or double quotes
print(greetings)    # Dumelang Sechaba
print(len(greetings)) # 16
sentence = "I hope you are learning Python"
print(sentence)

# Multiline_ string is created by using triple (''') or triple double quotes (""")

triple_single = '''I am a Software Developer and I am enjoying learning Python. I am finding
it rewarding for my career. That is why I am learning the 30 Days of Python'''
print(triple_single)

triple_double = """I am a Software Developer and I am enjoying learning Python. I am finding
it rewarding for my career. That is why I am learning the 30 Days of Python"""
print(triple_double)

# String Concatenation- we connect strings together (merging or connecting strings is called concatenation)

first_name = "Paseka"
last_name = "Swele"
space = ''
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Escape Sequence in Strings: \followed by a character is an escape sequence
# \n : new line
# \t : tab means(8 spaces)
# \\ : back slash
# \' : single quote
# \" : double quotes

print('I am enjoying learning the Python Challenge. \nAre you?') # line break
print('Days\tTopics\tExercises')  # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol(\\)')  # to write a backslash
print('In every programming language it starts with \"Hello World!\"')  # to write a dpuble quote inside a single quote

# Strings only

first_name = 'Gomolemo'
last_name = 'Swele'
language = 'Python'
formated_string = 'I am%s. I learn %s' %(first_name, last_name, language)
print(formated_string)

# strings and numbers 
radius = 10
pi = 3.14  # float digit
area = pi * radius ** 2 
formated_string = 'The area of a circle with a radius %d is %.2f.' %(radius, area)  # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formated_string = 'The following are Python libraries: %s' % (python_libraries)
print(formated_string)

# New style string formating (str.format)


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# String interpolation: is formatting a new string, f-strings- and we inject the data in their corresponding positions

a = 5
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}:.2f')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# unpacking characters

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# accessing characters in strings by Index: in programming counting starts from zero, meaning
# that the first letter of a string is zero index and the last letter of a string is the length of a string minus one

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# accessing the letter index from the right to left -1 will be the last index

language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# slicing a string- 

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#reversing a string 

greeting = "Dumelang Sechaba!"
print(greeting[::-1]) 

# skipping characters while slicing: skipping characters while slicing by passing step argument to slice method

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# String methods- that allow us to format strings

# capitalize()- converts the first letter of the string to a capital letter
challenge = 'thirty days of learning python'
print(challenge.capitalize())

# count- returns the occurrences of substring in a string
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`challenge = 'thirty days of python'

# endswith()- checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs()- replaces tab character with spaces, default tab size is 8
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# rfind(): returns the index of the last occurrence of a substring, if not found it returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# format()- formats string into a nicer output
first_name = 'Lucy'
last_name = 'Reatlegile'
age = 24
job = 'Software Developer'
country = 'South Africa'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

# index(): returns the lowest index of a substring, additional arguments indicate starting and ending index(default 0 and string length -1)
# if the substring is not found it raises a valueError
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error

# isalnum(): checks alphanumeric character- meaning the characters have no space between them
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): checks if all string elements are alphabet characters (a-z & A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal() checks if all chracters in a string are decimals (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

# isdigit(): checks if all characters in a string are numbers and some other unicode character of numbers
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

# isnumeric(): checks if all characters in a string are numbers or number related 
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

# isidentifier() checks for a valid identifier- checks if a is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): checks if all alphabets in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper()- checks if all alphabets in a string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join(): returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

# strip() removes all the given characters starting from the begining and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# replace() replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split()- strips the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title()- returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase- converts all uppercase characters to lowercase and all lowercase characters to upper characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): checks if string starts with the specified string
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False