def prime(n):
    prime=True
    is_Prime=lambda x,y:x%y==0
    for i in range(2,n):
        if(is_Prime(n,i)):
            prime=False
            break
    return prime
q=list(map(int,input().split()))
r=list(filter(prime,q))
print(r)