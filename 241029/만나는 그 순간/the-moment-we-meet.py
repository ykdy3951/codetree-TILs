n, m = map(int, input().split())

A = []
B = []

time = 0; pos = 0
for i in range(n):
    direction, dist = input().split()
    dist = int(dist)
    slope = (-1) ** (direction == 'L')
    npos = slope * dist + pos
    A.append([(slope, pos - (slope * time)), (time, time + dist)])
    time += dist
    pos = npos

time = 0; pos = 0
for j in range(m):
    direction, dist = input().split()
    dist = int(dist)
    slope = (-1) ** (direction == 'L')
    npos = slope * dist + pos
    B.append([(slope, pos - (slope * time)), (time, time + dist)])
    time += dist
    pos = npos

i, j = 1, 1
while i < n and j < m:
    a, b = A[i], B[j]

    aline, bline = a[0], b[0]
    arange, brange = a[1], b[1]

    if aline[0] - bline[0] == 0 and aline[1] - bline[1] == 0:
        print(max(arange[0], brange[0]))
        exit()
    
    if aline[0] - bline[0]:
        ans = (bline[1] - aline[1]) // (aline[0] - bline[0])
        
        if arange[0] <= ans <= arange[1] and brange[0] <= ans <= brange[1]:
            print(ans)
            exit()

    if arange[1] > brange[1]:
        j += 1

    elif arange[1] == brange[1]:
        i += 1; j += 1
    
    else:
        i += 1

print(-1)