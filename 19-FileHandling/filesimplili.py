import os 
file = open("C:/Simplilearn/today.txt", "r")
print(file.read())
file.close()

# read seven characters
import os 
file = open("C:/Simplilearn/today.txt", "r")
print(file.read(7))
file.close()

# reads one line 
import os
file = open("C:/Simplilearn/today.txt", "r")
print(file.readline())
file.close()

# read all ines 
import os
file = open("C:/Simplilearn/today.txt", "r")
print(file.readlines())
file.close()


import os
file = open("C:/Simplilearn/today.txt", "r")
print(file.readline(3))
file.close()


import os
file = open("C:/Simplilearn/today.txt", "w")
file.write("Sunday")
file.write("Monday")
file.close()

import os
file = open("C:/Simplilearn/today.txt", "x")
file.write("Lucy")
file.close

import os
os.remove("C:/Simplilearn/todya.txt")

import os 
if os.path.exists("C:/Simplilearn/today.txt"):
    os.remove("today.txt")
else: 
    print("There is no file with nmae today")

import os 
file = open("C:/Simplilearn/today.txt", "r")
for line in file:
    print(file.readline())
file.close()