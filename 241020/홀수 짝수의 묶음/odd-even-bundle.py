n=int(input())
l=[0]+list(map(int,input().split()))
for i in range(1, n+1):
    l[i]+=l[i-1]
ans=0

def bt(idx, last, flag, bundle):
    global ans
    if idx > n:
        ans=max(ans, bundle)
        return

    for i in range(idx, n+1):
        if flag and (l[i] - last) % 2:
            continue
        if not flag and (l[i] - last) % 2 == 0:
            continue

        bt(i+1, l[i], not flag, bundle + 1)
    
    return

bt(1, 0, True, 0)
print(ans)