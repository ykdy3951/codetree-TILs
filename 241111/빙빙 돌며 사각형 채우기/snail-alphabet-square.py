def snail_array(n, m):
    array = [[0] * m for _ in range(n)]
    num = 0
    x, y = 0, 0
    dx, dy = 0, 1

    while num <= n * m - 1:
        array[x][y] = chr(num % 26 + 65)
        num += 1
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x + dx, y + dy

    return array

n, m = map(int, input().split())
result = snail_array(n, m)
for row in result:
    print(*row)