l = [[0] * 201 for _ in range(201)]
for _ in range(int(input())):
    x1, y1 = map(int,input().split())
    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            l[i+100][j+100] = 1

print(sum(map(lambda x : sum(x), l)))