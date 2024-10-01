def solve_1(x, n):
    print(x, end=' ')

    if x == n:
        print()
        return

    solve_1(x + 1, n)

def solve_2(x, n):
    if x != n:
        solve_2(x + 1, n)
    print(x, end=' ')

n=int(input())
solve_1(1, n)
solve_2(1, n)