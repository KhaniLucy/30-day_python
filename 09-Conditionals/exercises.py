# 1. Get user input using input("Enter your age:"). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the amount of years
age = int(input("Enter your age"))
if age >= 18:
    print("You are old enough to drive!")
else: 
    years_left = 18 - age
    print("You need to wait {} more years before you can drive". format(years_left))