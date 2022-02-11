n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = i*j
        elif i == 0:
            a[i][j] = j
        elif j == 0:
            a[i][j] = i
#все условия бытты теперь ввыводим
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()