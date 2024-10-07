n = int(input())
l = []
t = 0
for _ in range(n):
    x, y = input().split()
    x = int(x)
    if y == 'L':
        l.append((t-x, t))
        t = t-x
    else:
        l.append((t, t+x))
        t = t+x

ans = [0] * 2001

for i in l:
    for j in range(i[0], i[1]):
        ans[j + 1000] += 1

cnt = 0
for i in ans:
    if i >= 2:
        cnt += 1
print(cnt)