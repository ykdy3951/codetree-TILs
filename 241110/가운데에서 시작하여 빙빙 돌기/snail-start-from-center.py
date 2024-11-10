n = int(input())
matrix = [[0] * n for _ in range(n)]
num = 1
x, y = n // 2, n // 2
matrix[x][y] = num
num += 1
dx, dy = 0, 1
for step in range(1, n):
    for _ in range(2):
        for _ in range(step):
            x += dx
            y += dy
            matrix[x][y] = num
            num += 1
        dx, dy = -dy, dx

for _ in range(n - 1):
    x += dx
    y += dy
    matrix[x][y] = num
    num += 1
for row in matrix:
    print(" ".join(map(str, row)))