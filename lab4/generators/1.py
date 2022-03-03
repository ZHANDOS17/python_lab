n = int(input())
def kvadrat (n):
    for i in range (n+1):
        yield i*i
for i in kvadrat(n):
    print(i, end =' ')