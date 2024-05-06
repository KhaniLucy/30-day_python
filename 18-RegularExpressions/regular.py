import re

pattern = re.compile("^[A-Z]+$")
print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("hello world"))

