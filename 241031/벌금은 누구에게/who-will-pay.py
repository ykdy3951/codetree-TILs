n,m,k=map(int,input().split())
l=[0] * n
for i in range(m):
    x = int(input())
    l[x-1] += 1
    if l[x-1] >= k:
        print(x)
        exit()
print(-1)