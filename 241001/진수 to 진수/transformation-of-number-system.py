a, b = map(int, input().split())
n = int(input())

x = 1
s = 0

while n:
    s += (n % 10) * x
    n //= 10
    x *= a

ans = ''

while s:
    ans += str(s % b)
    s //= b

print(ans[::-1])