n, t = map(int, input().split())
l = list(map(int, input().split()))
ans=0
tmp=0
for i in range(n):
    if l[i] > t:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0

print(max(ans, tmp))