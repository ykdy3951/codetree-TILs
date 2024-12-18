a, b = map(int, input().split())
c, d = map(int, input().split())

total_cleaned = (b - a) + (d - c) - max(0, min(b, d) - max(a, c))
print(total_cleaned)