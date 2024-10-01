def solve(a, b):
    if a < b:
        a *= 2
        b += 25
    else:
        a += 25
        b *= 2
    return a, b

a, b = map(int, input().split())
a, b = solve(a, b)
print(a, b)