r, c = map(int, input().split())
l = [list(map(lambda x : int(x == 'B'), input().split())) for _ in range(r)]

B = []
for i in range(r):
    for j in range(c):
        if l[i][j]:
            B.append((i, j))

ans = 0
# B
if l[0][0]:
    for b in B[1:]:
        if b[0] >= 2 and b[1] >= 2 and b[0] < r - 1 and b[1] < c - 1:
            ans += (b[0] - 1) * (b[1] - 1)
# W
else:
    for b in B[:-1]:
        if b[0] >= 1 and b[1] >= 1 and b[0] < r - 2 and b[1] < c - 2:
            ans += (r - 2 - b[0]) * (c - 2 - b[1])

print(ans)