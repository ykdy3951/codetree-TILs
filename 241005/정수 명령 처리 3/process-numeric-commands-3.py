from collections import deque

d = {
    'push_back': 'append',
    'push_front': 'appendleft',
    'pop_front': 'popleft',
    'pop_back': 'pop'
}

l = deque()

for _ in range(int(input())):
    x = input().split()
    if x[0] == 'front':
        print(l[0])
    elif x[0] == 'back':
        print(l[-1])
    else:
        if x[0] in d.keys():
            if len(x) == 2:
                getattr(l, d[x[0]])(x[1])
            else:
                print(getattr(l, d[x[0]])())
        else:
            if x[0] == 'size':
                print(len(l))
            else:
                print(int(len(l) == 0))