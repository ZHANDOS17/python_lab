import re

def lower_to_upper(s):
    return s.title()
    

snake = input()
camel = re.sub('_', ' ', snake)
y = re.sub(' ', '', lower_to_upper(camel))
print(y)
