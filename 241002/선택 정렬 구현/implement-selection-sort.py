n=int(input());l=list(map(int,input().split()))
for i in range(n-1):
    x=i
    for j in range(i+1,n):
        if l[j] < l[x]:
            x=j
    l[x],l[i]=l[i],l[x]
print(*l)