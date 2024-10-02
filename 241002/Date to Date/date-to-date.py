l=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(12):
    l[i+1]+=l[i]
a,b,c,d=map(int,input().split())
print(l[c-1]+d-l[a-1]-b+1)