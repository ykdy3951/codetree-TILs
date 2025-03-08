n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] += grid[i-1][j-1] + arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

ans = 0
for i in range(n-2):
    for j in range(n-2):
        ans = max(ans, arr[3+i][3+j] + arr[i][j] - arr[i+3][j] - arr[i][j+3])
print(ans)