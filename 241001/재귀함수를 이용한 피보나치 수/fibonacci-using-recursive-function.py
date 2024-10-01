l = [0] * 21
l[1] = l[2] = 1
def solve(n):
    if l[n]:
        return l[n]
    
    l[n] = solve(n-1) + solve(n-2)
    return l[n]

print(solve(int(input())))