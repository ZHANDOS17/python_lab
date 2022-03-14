import re

def text_replace(s):
    pattern = '[ .,]'
    res = re.sub(pattern, ":", s)
    print(res)

s = input()
text_replace(s)