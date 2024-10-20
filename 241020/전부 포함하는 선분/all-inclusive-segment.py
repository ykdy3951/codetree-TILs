l=[list(map(int,input().split())) for _ in range(int(input()))]

l.sort()
minX = [l[0][0], l[1][0]]
l.sort(key=lambda x : -x[1])
maxX = [l[0][1], l[1][1]]
print(min(maxX[0] - minX[1], maxX[1]-minX[0]))