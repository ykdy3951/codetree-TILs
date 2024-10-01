def solve(l, m):
    ans = 0
    while m >= 1:
        ans += l[m - 1]
        m = m - 1 if m % 2 else m // 2
    return ans 

n,m=map(int,input().split())
print(solve(list(map(int, input().split())), m))