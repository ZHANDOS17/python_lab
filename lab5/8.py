import re

def splitupper(s):
    x = re.findall("[A-Z][a-z]*", s)
    y = ' '.join(x)
    return y

s = input()  
print(splitupper(s))