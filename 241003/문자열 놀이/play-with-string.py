s,b=input().split()
s=list(s);b=int(b)
for _ in range(b):
    x,y,z=input().split()
    if x == '1':
        y, z = int(y)-1, int(z)-1
        s[y], s[z] = s[z], s[y]
        print(''.join(s))
    else:
        s=list(map(lambda a: z if a == y else a, s))
        print(''.join(s))