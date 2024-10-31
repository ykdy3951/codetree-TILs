a, b, c = map(int, input().split())
ans = 0

a_cnt = c // a
b_cnt = b // b

x, y = a_cnt, 0
while y <= b_cnt or x > 0:
    ans = max(ans, a * x + b * y)

    x -= 1
    if a * x + b * (y + 1) <= c:
        y += 1
print(ans)