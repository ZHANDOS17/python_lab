k = input()
s = list(map(int, k.split()))
x = 1
while 0 in s and x:
    p = s.index(0)
    if len(s)-1==p:
        break 
    x=0
    for i in range(1, p):
      if i + s[i]>p:
            s[p] = p-i
            x=1
            break
             
print(x)