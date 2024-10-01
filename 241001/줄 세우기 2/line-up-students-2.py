n = int(input())
l = []

for i in range(n):
    h, w = map(int, input().split())
    l.append([h, -w, i + 1])

l.sort()

for i in l:
    i[1] = -i[1]
    print(' '.join(map(str, i)))