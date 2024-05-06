"""FILE HANDLING"""
'''In python we have different data types.
Data is stored in different file formats.
To handle files we will also see different formats(.txt, .json, .xml, .csv, .tsv, .excel)

File handling is an important part of programming which allows us to create, read, update, and delete files.
In Python to handle data we use open() built-in function.'''

# syntax 
#  open('filename', mode)

# "r"-Read: default value. opens file for reading, it returns an error if the file does not exist.
# "a"-Append: opens a file for appending, creates the file if it does not exist.
# "w"-Write: opens a file for writing, creates the file if it does not exist.
# "x"-Create: creates a specified file, returns an error if the file exists.
# "t"-Text: default value. text mode
# "b"- Binary: binary mode (e.g. images)


'''Open files for Reading'''
# the default mode of open is reading, so we do not have to specify 'r' or 'rt'
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# read(): reads the whole text as a string
# to limit the number of characters we can pass an int value to the read(number) method.
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# printing the first 10 characters of the text file.
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first line
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# another way to get all the lines as a list is using splitlines()
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()


'''Opening Files for Writing and Updating'''
# to write an existing file, we must add a mode as a parameter to the open() function:
# "a"-Append: will append to the end of the file, if the file does not its creates a new file.
# "w"-Write: will overwrite any exisiting content, if the file does not exist it creates

# appending some text to the file we have been reading
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

# This method creates a new file, if the file does not exist
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')


'''DELETING FILES'''
# if you want to remove a file we use os module
import os
os.remove('./files/example.txt')

# if the file does not exist, the remove method will raise an error, so it is good to use a condition like this:
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')


""""FILE TYPES"""

'''File with txt Extension'''
# is a very common form of data and we have covered it in the previous section

'''File with json Extension'''
# JSON= JavaScript Object Notation. 
# it is a stringified JavaScript object or Python dictionary.

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''


'''Changing JSON to Dictionary'''
# to change a JSON to a dictionary, first we import the json module and then we use loads method

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


'''Changing Dictionary to JSON'''
# to change a dictionary to a JSON we use dumps method from the json module.

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)


'''Saving as JSON File'''
# we can also save our data as a json file.
# for writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
# we use encoding and indentation. Indentation makes the json file easy to read.


'''File with csv Extension'''
# csv= Comma Separated Values. 
# CSV is a simple file format used to store tabular data, such as a spreadsheet or database
# csv is a very common data format in data science.

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')


'''File with xlsx Extension'''
# to read excel files we need to install xlrd pacakge.
'''import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)'''


'''File with xml Extension'''
# XML is another structured data format which looks like HTML.
# in XML the tags are not predefined.
# first line is an XML declaration.
'''<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>'''


import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)