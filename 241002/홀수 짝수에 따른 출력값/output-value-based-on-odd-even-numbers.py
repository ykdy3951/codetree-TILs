n=int(input())

if n % 2:
    n = (n + 1) // 2
    print(n * n)
else:
    n //= 2
    print(n * n + n)