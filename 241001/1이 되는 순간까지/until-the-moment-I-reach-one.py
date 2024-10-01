def solve(n) -> int:
    if n == 1:
        return 0
    if n % 2:
        cnt = solve(n // 3)
    else:
        cnt = solve(n // 2)
    return 1 + cnt

print(solve(int(input())))