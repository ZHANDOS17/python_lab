a = input().split()
for i in range(len(a)):
    a[i]=int(a[i])

def filter_prime(a):
    t = []
    for j in a:
        cnt=0
        for i in range(2, j):
            if j%i==0:
                cnt+=1
        if cnt==0:
            t.append(j)
    return t 

filter_prime(a)