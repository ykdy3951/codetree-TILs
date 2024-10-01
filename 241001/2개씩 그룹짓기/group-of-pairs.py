n=int(input());l=sorted(list(map(int,input().split())))

ans = 2000
for i in range(n):
    ans = min(ans, l[i] + l[2*n-1-i])

print(ans)