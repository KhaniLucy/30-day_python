# Variables in Python

first_name = 'Lucy'
last_name = 'Swele'
country = 'South Africa'
city = "Soweto"
age = 24
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python', 'Bootstrap']
personal_info = {
    'firstname' : 'Makhananisa',
    'lastname' : 'Swele',
    'country' : 'South Africa',
    'city':'Soweto'
}

# Printing the variables stored in the variables

print('First name:', first_name)
print('First name length', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Skills:', skills)
print('Personal information:', personal_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Lucy', 'Swele', 'South Africa', 24, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country', country)
print('Age:', age)
print('Married:', is_married)