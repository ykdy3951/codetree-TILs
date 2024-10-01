def solve(n):
    if n == 0:
        return 0
    return (n % 10) ** 2 + solve(n // 10)
print(solve(int(input())))