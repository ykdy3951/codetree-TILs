n=int(input())

l = [0] * 101
l[1] = 2
l[2] = 4

def solve(n):
    if l[n] != 0:
        return l[n]

    l[n] = (solve(n-1) * solve(n-2)) % 100
    return l[n]

print(solve(n))