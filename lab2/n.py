s = []
while 1:
    a = int(input())
    if a==0:
        break
    s.append(a)
"""
for i in range( (int(len(s))+1)//2):
    if i!=len(s)-1-i:
        print(s[i]+s[len(s)-i-1])
    else:
        print(s[i])
        """
print(*[s[i]+s[len(s)-i-1] if i!=len(s)-1-i else s[i] for i in range((len(s)+1)//2)])   