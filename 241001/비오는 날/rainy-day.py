n=int(input())
l=[list(input().split()) for _ in range(n)]
for i in l:
    if i[-1] == 'Rain':
        print(' '.join(i))
        break