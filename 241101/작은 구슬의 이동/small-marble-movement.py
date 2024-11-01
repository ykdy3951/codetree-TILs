n, t = map(int,input().split())
r, c, d = input().split()
r, c = int(r), int(c)

D = {
    'R' : [0, 1],
    'U' : [-1, 0],
    'D' : [1, 0],
    'L' : [0, -1]
}

if d in 'LR':
    while t:
        if c == 1 or c == n:
            d = list(D.keys())[3-list(D.keys()).index(d)]
            t -= 1
            if t == 0:
                break
        r += D[d][0]
        c += D[d][1]
        
        t -= 1

else:
    while t:
        if r == 1 or r == n:
            d = list(D.keys())[3-list(D.keys()).index(d)]
            t -= 1
            if t == 0:
                break

        r += D[d][0]
        c += D[d][1]
        
        t -= 1
        
print(r, c)