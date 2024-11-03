n, t = map(int, input().split())
s = input()
l = [list(map(int,input().split())) for _ in range(n)]
x, y = n//2, n//2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
idx = 0
ans = l[x][y]
for i in s:
    if i == 'R':
        idx = (idx + 1) % 4
    elif i == 'L':
        idx = (idx - 1) % 4
    else:
        nx, ny = x + dx[idx], y + dy[idx]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        ans += l[nx][ny]
        x, y = nx, ny
print(ans)