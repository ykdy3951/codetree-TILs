n=int(input())
def solve(n):
    if n == 1:
        return 0
    if n % 2:
        return 1 + solve(n * 3 + 1)
    else:
        return 1 + solve(n // 2)

print(solve(n))