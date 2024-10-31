n=int(input())
l=list(map(int,input().split()))

ans = 1e10
for i in range(n):
    l[i] *= 2
    for j in range(n):
        tmp = l[0] if j != 0 else l[1]
        val = 0
        for k in range(1, n):
            if j == k:
                continue
            val += abs(l[k] - tmp)
            tmp = l[k]
        ans = min(ans, val)
    l[i] //= 2
print(ans)