a, b, n = [], [], int(input())
for i in range(n):
    s = list(input().split())
    x = int (a[0])
    if len(a) == 1: #2
        b.append(a[0])
        a.pop(0)
    if x ==1:
        b.append(a[1])
print(*b)