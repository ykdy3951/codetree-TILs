def solve(l, i, n):
    if i == n:
        return 0

    return max(l[i], solve(l, i + 1, n))

n = int(input())
l = list(map(int, input().split()))

print(solve(l, 0, n))