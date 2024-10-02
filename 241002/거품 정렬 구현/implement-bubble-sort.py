n=int(input());l=list(map(int,input().split()))
while True:
    is_sort = True
    for i in range(n-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            is_sort = False
    if is_sort:
        break
print(*l)