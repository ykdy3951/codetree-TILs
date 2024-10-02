l = [0] * 16
l[1] = 1
l[2] = 2

def solve(n):
    if l[n]:
        return l[n]
    l[n] = solve(n // 3) + solve(n - 1)
    return l[n]

print(solve(int(input())))