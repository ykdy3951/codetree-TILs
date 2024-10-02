from collections import deque

d = deque()

for _ in range(int(input())):
    x,y=input().split()
    y=int(y)

    if x == 'push_back':
        d.append(y)
    
    elif x[0] == 'g':
        print(d[k-1])
    elif x[0] == 's':
        print(len(d))
    else:
        d.pop()