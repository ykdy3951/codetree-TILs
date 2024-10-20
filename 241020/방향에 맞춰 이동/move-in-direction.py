mapping_idx = {'N':0,'E':1,'W':2,'S':3}
dx=[0, 1, -1, 0]
dy=[1, 0, 0, -1]

coord=[0,0]
for i in range(int(input())):
    direction, weight = input().split()
    weight = int(weight)
    
    idx = mapping_idx[direction]
    coord[0] += dx[idx] * weight
    coord[1] += dy[idx] * weight

print(*coord)