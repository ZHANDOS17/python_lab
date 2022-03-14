import re

def text_match(s):
    pattern = '[a-z]+_[a-z]+'
    if re.search(pattern, s):
        return 'A match!'
    else:
        return 'Not a match!'

s = input()
print(text_match(s))