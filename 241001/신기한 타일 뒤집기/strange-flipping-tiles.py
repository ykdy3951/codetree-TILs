n = int(input())
l = [0] * (200001)

idx = 100000

for i in range(n):
    x, y = input().split()
    y = 1 if y == 'L' else -1
    
    for j in range(int(x)-1):
        l[idx] = y
        idx += y
    l[idx] = y
ans = [0, 0]
for i in range(200001):
    if l[i] == 1:
        ans[0] += 1
    elif l[i] == -1:
        ans[1] += 1
print(ans[0], ans[1])