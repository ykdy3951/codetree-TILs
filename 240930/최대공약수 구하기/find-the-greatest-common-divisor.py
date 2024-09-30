def gcd(n : int, m : int) -> int:
    if n > m:
        n, m = m, n
    
    while n and m:
        m %= n
        if n > m:
            n, m = m, n
    
    return m

n, m = map(int,input().split())
print(gcd(n, m))