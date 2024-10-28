l = [[0] * 2002 for _ in range(2002)]

x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        l[i+1000][j+1000] = 1

x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        l[i+1000][j+1000] = 0

a = 0; b = 0
for i in range(2002):
    st, end = 0, 0
    for j in range(2002):
        if l[i][j]:
            st, end = j, j
            break

    for j in range(2001, -1, -1):
        if l[i][j]:
            end = j
            break
    
    a = max(end - st + 1, a)

for i in range(2002):
    st, end = 0, 0
    for j in range(2002):
        if l[j][i]:
            st, end = j, j
            break
        
    for j in range(2001, -1, -1):
        if l[j][i]:
            end = j
            break

    b = max(end - st + 1, b)

print(a * b)