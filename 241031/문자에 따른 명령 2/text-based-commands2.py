dx=[0,1,0,-1]
dy=[1,0,-1,0]
idx=0

coord = [0, 0]
for i in input():
    if i == 'L':
        idx = (idx - 1) % 4
    elif i == 'R':
        idx = (idx + 1) % 4
    else:
        coord[0] += dx[idx]
        coord[1] += dy[idx]
print(*coord)