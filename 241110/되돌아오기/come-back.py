x = 0
y = 0

D = {
    'N' : [0, 1],
    'S' : [0, -1],
    'W' : [-1, 0],
    'E' : [1, 0]
}

ans = 0
for i in range(int(input())):
    d, s = input().split()
    s = int(s)
    while s:
        s -= 1
        ans += 1
        x += D[d][0]
        y += D[d][1]

        if x == y == 0:
            print(ans)
            exit()
print(-1)