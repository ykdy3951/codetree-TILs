def laser_reflection(N, grid, K):
    
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    if 1 <= K <= N:
        x, y, d = 0, K - 1, 2
    elif N < K <= 2 * N:
        x, y, d = K - N - 1, N - 1, 3
    elif 2 * N < K <= 3 * N:
        x, y, d = N - 1, 3 * N - K, 0
    else:
        x, y, d = 4 * N - K, 0, 1

    reflection_count = 0

    while 0 <= x < N and 0 <= y < N:
        if grid[x][y] == '/':
            d = [1, 0, 3, 2][d]
        else:
            d = [3, 2, 1, 0][d]
        
        reflection_count += 1
        x, y = x + directions[d][0], y + directions[d][1]

    return reflection_count

N = int(input())
grid = [list(input()) for _ in range(N)]
K = int(input())

print(laser_reflection(N, grid, K))