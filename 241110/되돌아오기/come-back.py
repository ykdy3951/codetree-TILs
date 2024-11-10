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
    x += D[d][0]
    y += D[d][1]
    ans += int(s)

    if x == y and y == 0:
        print(ans)
        break