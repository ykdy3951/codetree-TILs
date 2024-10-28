n=int(input())
l = [[0] * 202 for _ in range(202)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            l[j+100][k+100] = (i % 2)

print(sum(map(lambda x : sum(x), l)))