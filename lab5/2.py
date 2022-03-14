import re
def text_match(s):
    pattern = 'ab{2,3}'
    if re.search(pattern, s):
        return 'A match!'
    else:
        return 'Not a match'
s = input()
print(text_match(s))
