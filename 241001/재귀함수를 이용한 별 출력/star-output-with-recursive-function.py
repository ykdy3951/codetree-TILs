def solve(i, n):
    print('*'*i)
    if i != n:
        solve(i+1, n)

solve(1, int(input()))