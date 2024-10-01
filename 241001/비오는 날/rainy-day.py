n=int(input())
l=[list(input().split()) for _ in range(n)]
l.sort()
for i in l:
    if i[-1] == 'Rain':
        print(' '.join(i))
        break