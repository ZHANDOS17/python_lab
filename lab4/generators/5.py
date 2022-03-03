n = int(input())
def kersinwe (n):
    for i in range (n+1):
        yield i
for i in kersinwe(n):
    print(n-i, end =' ')