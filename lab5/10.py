import re

def lower(s):
    return s.lower()

s = input()
print(re.sub(' ', '_', lower(s)))