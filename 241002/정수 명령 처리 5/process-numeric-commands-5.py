from collections import deque

d = deque()

for _ in range(int(input())):
    x=input()

    if x[:9] == 'push_back':
        d.append(x.split()[1])
    elif x[0] == 'g':
        print(d[int(x.split()[1])-1])
    elif x[0] == 's':
        print(len(d))
    else:
        d.pop()