a = list(map(int, input().split()))
if len(a)!=1:
    n, x = a[0], a[1]
else:
    n = a[0];x = int(input())     
t=x
for i in range(1, n):
    t^=x+2*i
print(t)
#5 0
#print (0^2^4^6^8)