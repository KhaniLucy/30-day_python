"""Need for exception Handling"""
# the program terminates whenever an error occurs
# sudden termination can corrupt the program
# exception may cause data loss
'''helps to have a clean program even when execution of the program happens it thows errors'''


'''Exception: is a runtime error that terminates the execution of a program'''

'''Execption handling'''
# generates a message in correspondence to the occurrence of an error and takes the right step to handle it

'''three types of errors'''
# compile time error
# logical errors
# run time errors: difficult to track


''''Points to remember when Exception Handling'''
# 1. You can write try block without any except blocks
# 2. You can write several execpt blocks for a single try block
# 3. You can write multiple except blocks to handle multiple exceptions
# 4. You can write exception as an object
# 5. You can write multiple exception within tuple


# Divide by Zero Error
a = 10
b = 0
c = a/b
print("a/b = %" %c)
# output will be a Zero Division Error: and this is an unhandled exception


# handlding the zero division error
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
except:
    print("Can't divide with zero")


a = 70
b = 0
try:
    print(a/b)
    print("New Line")
except ZeroDivisionError:
    print("Do not divide number by zero")
print("completed")


a = 70
b = 9
try:
    print(a/b)
    print("New Line")
except ZeroDivisionError:
    print("Don't divide by zero")
print("Completed")


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = %d"%c)
except Exception:
    print("Can't divide by zero")
    print(Exception)
else:
    print("SIMPLILEARN")


# capturing an exception in a variable
a = 10
b = 0
try:
    print(a/b)
except Exception as a:
    print("Do not divide number by zero", a)
print("Completed")


"""a = 10
b = 0
try:
    print(a/z)
except Exception as a:
    print("Do not divide number by zero", a)
except NameError as b:
    print(b)
print("Completed")"""


try:
    a = 5
    b = 0
    print(a/b)
except TypeError:
    print("Unsupported operation")
except ZeroDivisionError:
    print('Division by zero is not allowed')

