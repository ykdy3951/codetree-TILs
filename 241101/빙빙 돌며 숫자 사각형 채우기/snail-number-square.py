n, m = map(int, input().split())

l = [[1] + ([0] * m) + [1] for i in range(n)]
l.append([1] * (m + 2))

cnt = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 1
i = 0

while cnt <= n * m:
    l[x][y] = cnt
    cnt += 1
    nx, ny = x + dx[i], y + dy[i]
    if l[nx][ny]:
        i = (i + 1) % 4
    x, y = x + dx[i], y + dy[i]

for i in range(n):
    print(*l[i][1:-1])