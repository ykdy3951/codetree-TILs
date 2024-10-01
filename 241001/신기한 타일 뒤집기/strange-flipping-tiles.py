n = int(input())
l = [0] * 101
for _ in range(n):
    x, cnt = input().split()
    x = int(x)
    cnt = 1 if cnt == 'L' else 2
    for i in range(x):
        l[i] = cnt
    
ans = [0, 0]
for i in range(101):
    if l[i] == 0:
        break
    ans[l[i]-1]+=1
print(' '.join(map(str,ans)))