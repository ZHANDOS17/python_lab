n = int(input())
def jup_san (n):
    for i in range (n+1):
        if not i % 2:
           yield i
for i in jup_san(n):
    print(i, end =', ')