import re
def text_match(s):
    patterns = '^a(b*)$'
    if re.search(patterns, s):
        return 'A match!'
    else:
        return ('Not a match!')
s = input()
print(text_match(s))
