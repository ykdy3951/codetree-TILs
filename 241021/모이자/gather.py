n=int(input())
l=list(map(int,input().split()))
l=[[i, l[i]] for i in range(n)]
ans=1000000
for i in range(n):
    ans=min(ans, sum(map(lambda x: abs(x[0]-i)*x[1], l)))
print(ans)