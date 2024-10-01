n, m = map(int, input().split())
l = [0] + list(map(int, input().split()))
for i in range(n):
    l[i+1] += l[i]

for _ in range(m):
    s, e = map(int, input().split())
    print(l[e]-l[s-1])