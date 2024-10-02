n=int(input());l=list(map(int,input().split()))
for i in range(n-1):
    x=i
    t=l.index(min(l[i:]))
    l[i],l[t]=l[t],l[i]
print(*l)