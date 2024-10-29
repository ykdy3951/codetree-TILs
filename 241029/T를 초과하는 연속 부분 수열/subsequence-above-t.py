n, t = map(int, input().split())
l = list(map(int, input().split()))
ans=0
tmp=int(l[0] > t)
for i in range(1, n):
    if l[i] > l[i - 1] and l[i] > t:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = int(l[0] > t)

print(max(ans, tmp))