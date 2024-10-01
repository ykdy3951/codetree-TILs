def solve(i):
    print('* ' * i)
    if i > 1:
        solve(i-1)
    print('* ' * i)
solve(int(input()))