def count_lee(grid, n, m):
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (0, -1),
        (-1, 0),
        (-1, -1)
    ]
    count = 0
    for i in range(n):
        for j in range(m):
            for dx, dy in directions:
                if 0 <= i + 2 * dx < n and 0 <= j + 2 * dy < m:
                    if (
                        grid[i][j] == 'L' and
                        grid[i + dx][j + dy] == 'E' and
                        grid[i + 2 * dx][j + 2 * dy] == 'E'
                    ):
                        count += 1
    return count

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
result = count_lee(grid, n, m)
print(result)