import re
s = input()
s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
print(s)