def solve(i):
    print(i, end=' ')
    if i > 1:
        solve(i - 1)
    print(i, end=' ')
solve(int(input()))