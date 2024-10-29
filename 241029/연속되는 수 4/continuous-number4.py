n=int(input())
l=[int(input()) for _ in range(n)]
ans=0
tmp=1
for i in range(1, n):
    if l[i] > l[i - 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 1

print(max(ans, tmp))