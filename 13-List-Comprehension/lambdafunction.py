"""LAMBDA FUNCTION"""
# is an anonymous function defined without a name or a def keyword
# lambda function can take any number of arguments but can only have one expression

def add(a,b):
    result = a + b
    return result

add (3, 4)
print(add)


# using lambda method
add = lambda a,b : a+ b
add(3, 4)


# passing one argument
add = lambda x : x + 100
print(add(50))


# directlying calling lambda
(lambda a, b : a * b)(5, 7)
# known as = immediatley invoked function expression


# keyboard arguments using lambda
product = lambda x, y, z, : x*y*z
print(product(z=5, x=10, y=4))


# default arguments
add = lambda x,y = 15, z = 24 : x+y+z
print(add(20))


# using asterik parameter
addition = lambda *args : sum(args)
print(addition(20, 2, 40, 50))


# higher order function
higher_ord_fun = lambda x, fun : x + fun(x)
higher_ord_fun(20, lambda x : x*x)


# display order even
(lambda x : (x % 2 and 'odd' or 'even'))(10)


# lambda that checks if a string is a substring of the given string
sub_string = lambda string : string in "Welcome to Python Functions Tutorial"
print(sub_string('java'))
# output will be false


# using lambda function using filter function
num = [10, 40, 56, 27, 33, 15, 70]
greater = list(filter(lambda num : num > 30, num))
print(greater)


# filtering a list of numbers that are divisible by four
list1 = [10, 40, 56, 27, 33, 15, 70]
divide = list(filter(lambda x : (x%4 == 0), list1))
# output is 40, 56


# exploring how to using the map function along with lambda function
list2 = [10, 40, 56, 27, 33, 15, 70]
double_the_num = list(map(lambda x : x*2, list2))
print(double_the_num)
# output everynumber on the list will be multiplied by two


# finding the power of the number
list3 = [2,5,10,6,4,12]
cube = map(lambda x : pow(x,3), list3)
list(cube)


# how to using the reduced function in python along with the lambda function
from functools import reduce
list4 = [2,5,10,6,4,12]
sum = reduce((lambda x, y : x+y), list4)
print(sum)


# lambda function in a defined function
def quadratic(a,b,c):
    return lambda x : a*x**2 + b*x +c
f = quadratic(2,3,5)
f(2)
