n = int(input())
def trichetyre (n):
    for i in range (n+1):
        if not i %3 and not i%4:
           yield i
for i in trichetyre(n):
    print(i, end =', ')