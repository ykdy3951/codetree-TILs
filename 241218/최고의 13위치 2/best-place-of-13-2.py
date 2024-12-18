from itertools import combinations

def sum_subgrid(grid, x, y, N):
    if y + 2 < N:
        return grid[x][y] + grid[x][y+1] + grid[x][y+2]
    return 0

def are_disjoint(a, b):
    return not (set(a) & set(b))

def max_coins(grid, N):
    regions = []

    for i in range(N):
        for j in range(N - 2):
            region = [(i, j), (i, j+1), (i, j+2)]
            regions.append((region, sum_subgrid(grid, i, j, N)))

    max_coins = 0

    for (region1, sum1), (region2, sum2) in combinations(regions, 2):
        if are_disjoint(region1, region2):
            max_coins = max(max_coins, sum1 + sum2)

    return max_coins

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
print(max_coins(grid, N))