n = int(input())
l = [[0] * 201 for _ in range(201)]
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            l[i+100][j+100] = 1
    
print(sum(map(lambda x : sum(x), l)))