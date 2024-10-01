def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(l, n, i):
    if i == n - 1:
        return l[i]
    
    return lcm(l[i], solve(l, n, i + 1))

n = int(input())
l = list(map(int, input().split()))
print(solve(l, n, 0))