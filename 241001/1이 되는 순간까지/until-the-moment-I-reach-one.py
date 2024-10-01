def solve(n) -> int:
    if n == 1:
        return 1
    if n % 2:
        cnt = solve(n // 2)
    else:
        cnt = solve(n // 3)
    return 1 + cnt

print(solve(int(input())))