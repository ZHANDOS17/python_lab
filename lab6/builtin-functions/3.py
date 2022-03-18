from operator import truediv


n = input()
l = ''.join(reversed(n))
if n == l: 
    print(True)
else:
    print(False)
