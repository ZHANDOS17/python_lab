a = int(input())
n = int(input())
def squares (a,n):
    for i in range (a,n+1):
        yield i*i
for i in squares(a,n):
    print(i, end =' ')