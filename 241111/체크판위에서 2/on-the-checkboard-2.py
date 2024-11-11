r, c = map(int, input().split())
l = [list(map(lambda x : int(x == 'B'), input().split())) for _ in range(r)]

B = []
for i in range(r):
    for j in range(c):
        if l[i][j]:
            B.append((i, j))

ans = 0
# B
if l[0][0] and l[-1][-1] == 0:
    for b in B[1:]:
        if b[0] >= 2 and b[1] >= 2 and b[0] < r - 1 and b[1] < c - 1:
            for i in range(1, b[0]):
                for j in range(1, b[1]):
                    if l[i][j] == 0:
                        ans += 1
# W
elif l[0][0] == 0 and l[-1][-1]:
    for b in B[:-1]:
        if b[0] >= 1 and b[1] >= 1 and b[0] < r - 2 and b[1] < c - 2:
            for i in range(b[0]+1, r-1):
                for j in range(b[1]+1, c-1):
                    if l[i][j] == 0:
                        ans += 1

print(ans)