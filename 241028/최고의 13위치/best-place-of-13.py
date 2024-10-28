n=int(input())
l=[[0]+list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, n+1):
        l[i][j] += l[i][j-1]

ans = 0
for i in range(n):
    for j in range(3, n+1):
        ans = max(ans, l[i][j]-l[i][j-3])
print(ans)