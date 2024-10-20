l=sorted(list(map(int,input().split())))
print(l[0], l[1], l[2], l[-1]-sum(l[:3]))