n, m = map(int, input().split())
l = [[0] * n for _ in range(n)]
d = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]
for i in range(m):
    x, y = map(int, input().split())
    l[x-1][y-1] = 1
    cnt = 0
    for z in d:
        nx, ny = x + z[0] - 1, y + z[1] - 1
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if l[nx][ny]:
            cnt += 1
    if cnt >= 3:
        print(1)
    else:
        print(0)