x = 0
y = 0

D = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
ans = 0
idx = 0
for i in input():
    ans += 1
    if i == 'L':
        idx = (idx - 1) % 4
    elif i == 'R':
        idx = (idx + 1) % 4
    else:
        x += D[idx][0]
        y += D[idx][1]
        if x == y == 0:
            print(ans)
            exit()

print(-1)